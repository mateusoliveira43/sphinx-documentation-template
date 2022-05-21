"""Example of a class."""


class PersonExample:
    """Person with a name and with or without a dog."""

    def __init__(
        self,
        name: str,
        has_dog: bool = False,
    ) -> None:
        """
        Initiate person class.

        Parameters
        ----------
        name : str
            Name of the person.
        has_dog : bool, optional
            If the person has or not a dog, by default False.

        """
        self.name = name
        self.has_dog = has_dog

    def get_person_information(self) -> str:
        """
        Get person information.

        Returns
        -------
        str
            Person info.

        """
        return (
            f"Person {self.name} has a dog! :)"
            if self.has_dog
            else f"Person {self.name} does not a dog. :("
        )

    def adopt_dog(self) -> None:
        """Adopt a dog."""
        self.has_dog = True
