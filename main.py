from selenium.webdriver.support.expected_conditions import element_located_selection_state_to_be

import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    taxi_container = (By.CLASS_NAME, 'type-picker shown')
    button_ask_taxi = (By.CLASS_NAME, 'button round')
    comfort_option = (By.XPATH, '//div[@class="tcard-title"][normalize-space(text())="Comfort"]')
    phone_number =  (By.XPATH, '//div[@class="np-text][normalize-space(text())="Número de teléfono"]')
    modal_phone_number = (By.ID, 'phone')
    next_button_modal_phone_number = (By.XPATH, '//div[@class="buttons"]/button[text()="Siguiente"]')
    modal_sms_code = (By.XPATH, '//input[@value="1223"]')
    modal_button_submit = (By.XPATH, '//button[text()="Confirmar"]')
    card_payment = (By.XPATH, '//div[@class="pp-text"][normalize-space(text())="Método de pago"]')
    add_card  = (By.XPATH, '//div[@class="pp-title"][normalize-space(text())="Agregar tarjeta"]')
    card_number = (By.ID,'number')
    cvv = (By.ID, 'code')
    button_cvv_add = (By.XPATH, '//button[@class="button full"][normalize-space(text())="Agregar"]')
    sms_driver = (By.ID, 'comment')
    switch_button_1 = (By.XPATH, '//div[@class="switch"]/span[@class="slider round"]')
    switch_button_2 = (By.XPATH, '//div[@class="r-sw"]/div[@class="switch"]/span[@class="slider round"]')
    counter_ice_cream = (By.XPATH, '//div[contains(@class,"r-counter-label") and text()="Helado"]/following-sibling::div//div[@class="counter-plus"]')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    # Esperar a que el contenedor "type-picker shown" aparezca después de ingresar las direcciones
    def wait_for_load_taxi_container(self):
        WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located(self.taxi_container))

    # Esperar a que el boton "Pedir Taxi" aparezca en el contenedor "type-picker shown" aparezca después de ingresar las direcciones y darle click
    def wait_for_load_button_ask_taxi(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.button_ask_taxi)).click()

    # Esperar a que el elemento "Comfort" aparezca y luego se da click sobre el
    def wait_for_comfort_option(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            # Esperar a que el elemento esté en el DOM y sea visible
            element = wait.until(expected_conditions.visibility_of_element_located(self.comfort_option))
            # Luego esperar a que el elemento sea clickeable
            element = wait.until(expected_conditions.element_to_be_clickable(self.comfort_option))
            # Hacer click sobre el elemento
            element.click()
            #Se atrapa un error en la variable "e" en caso de que ocurra en el bloque try
        except Exception as e:
            print(f"Error: {e}")

     # Esperar a que el elemento "Número de telefono" aparezca y luego se da click sobre el
    def wait_for_phone_number_option(self):
        try:
            wait = WebDriverWait(self.driver,10)
            # Esperar a que el elemento esté en el DOM y sea visible
            phone_number_element = wait.until(EC.visibility_of_element_located(self.phone_number))
            # Luego esperar a que el elemento sea clickeable
            phone_number_element = wait.until(EC.element_to_be_clickable(self.phone_number))
            # Hacer click sobre el elemento
            phone_number_element.click()
            # Se atrapa un error en la variable "e" en caso de que ocurra en el bloque try
        except Exception as e:
            print(f"Error: {e}")

    # Esperar a que el elemento "Número de telefono" aparezca y luego se da click sobre el
    def wait_for_phone_number_modal(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            # Esperar a que el elemento esté en el DOM y sea visible
            phone_number_modal = wait.until(EC.visibility_of_element_located(self.modal_phone_number))
            # Luego esperar a que el elemento sea clickeable
            phone_number_modal = wait.until(EC.element_to_be_clickable(self.modal_phone_number))
            # Hacer click sobre el elemento
            phone_number_modal.click()
            # Se atrapa un error en la variable "e" en caso de que ocurra en el bloque try
        except Exception as e:
            print(f"Error: {e}")

    # Introducir el número de telefono
    def set_phone_number(self, phone_number_settled):
        self.driver.find_element(*self.phone_number).send_keys(phone_number_settled)

    #Buscar el boton "Siguiente" y darle click
    def click_on_next_button(self):
        self.driver.find_element(*self.next_button_modal_phone_number).click()

    # Esperar a que el elemento "Introducir código" aparezca y luego se da click sobre el
    def wait_for_code_input(self):
        try:
            wait = WebDriverWait(self.driver,10)
            # Esperar a que el elemento esté en el DOM y sea visible
            code_element = wait.until(EC.visibility_of_element_located(self.modal_sms_code))
            # Luego esperar a que el elemento sea clickeable
            code_element = wait.until(EC.element_to_be_clickable(self.modal_sms_code))
            # Hacer click sobre el element
            code_element.click()
        except Exception as e:
            print(f"Error: {e}")

    # Introducir el número de código
    def set_code(self, code):
        self.driver.find_element(*self.modal_sms_code).send_keys(code)

    # Buscar el boton "Confirmar" y darle click
    def click_on_submit_button(self):
        self.driver.find_element(*self.modal_button_submit).click()

    # Esperar a que el elemento "Metodo de pago" aparezca y luego se da click sobre el
    def wait_for_payment_method(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            # Esperar a que el elemento esté en el DOM y sea visible
            payment_element = wait.until(EC.visibility_of_element_located(self.card_payment))
            # Luego esperar a que el elemento sea clickeable
            payment_element = wait.until(EC.element_to_be_clickable(self.card_payment))
            # Hacer click sobre el element
            payment_element.click()
        except Exception as e:
            print(f"Error: {e}")

    # Esperar a que el elemento "Agregar tarjeta" aparezca y luego se da click sobre el
    def wait_for_add_card(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            # Esperar a que el elemento esté en el DOM y sea visible
            add_card_element = wait.until(EC.visibility_of_element_located(self.add_card))
            # Luego esperar a que el elemento sea clickeable
            add_card_element = wait.until(EC.element_to_be_clickable(self.add_card))
            # Hacer click sobre el element
            add_card_element.click()
        except Exception as e:
            print(f"Error: {e}")

    # Esperar a que el elemento "Número de la tarjeta" aparezca y luego se da click sobre el y se rellena
    def wait_for_add_card_number(self, number_card):
        try:
            wait = WebDriverWait(self.driver, 10)
            # Esperar a que el elemento esté en el DOM y sea visible
            add_card_number_element = wait.until(EC.visibility_of_element_located(self.card_number))
            # Luego esperar a que el elemento sea clickeable
            add_card_number_element = wait.until(EC.element_to_be_clickable(self.card_number))
            # Hacer click sobre el element
            add_card_number_element.click()
            # Introducir número de tarjeta
            add_card_number_element.send_keys(number_card)
        except Exception as e:
            print(f"Error: {e}")

    # Rellenar el CVV
    def set_cvv_number(self, cvv_number):
        cvv_element = self.driver.find_element(*self.cvv).send_keys(cvv_number)
        # Simulacion de la tecla TAB para perder el enfoque (activar validaciones)
        cvv_element.send_keys(Keys.TAB)
        # Esperar a que el botón "Agregar" sea clickeable
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.button_cvv_add))

    #Escribir mensaje al conductor
    def set_sms_to_driver(self, sms):
        # Esperar a que el elemento sea clickeable y darle click
        wait = WebDriverWait(self.driver, 10)
        sms_element = wait.until(EC.element_to_be_clickable(self.sms_driver))
        sms_element.click()
        # Limpiar el campo si tiene texto predefinido
        sms_element.clear()
        #Escribir el mensaje
        sms_element.send_keys(sms)

    # Pedir otras opciones
    def ask_for_more_options(self):
        wait = WebDriverWait(self.driver, 10)
        # Pedir una manta y pañuelos
        blanket_and_tissues_switch = wait.until(EC.element_to_be_clickable(self.switch_button_1))
        blanket_and_tissues_switch.click()
        # Verificar si el switch está activado
        is_blanket_and_tissues_selected = blanket_and_tissues_switch.is_selected()
        # Pedir cortina acustica
        acoustic_curtain_switch = wait.until(EC.element_to_be_clickable(self.switch_button_2))
        acoustic_curtain_switch.click()
        # Verificar si el switch está activado
        is_acoustic_curtain_selected = acoustic_curtain_switch.is_selected()

    #Pedir 2 helados
    def ask_for_ice_cream(self, quantity):
        # Localizar el contenedor del helado
        ice_cream_container = self.driver.find_element(self.counter_ice_cream)

        # Hacer clic en el botón "+" hasta alcanzar la cantidad deseada (2)
        current_value = 0
        while current_value < quantity:
            ice_cream_container.click()
            current_value += 1

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(desired_capabilities=capabilities)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to

        #Lllamar a los metodos
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)

        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
