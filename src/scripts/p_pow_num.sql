CREATE OR REPLACE PROCEDURE p_pow_num(
	_num int,
	_power int,
	INOUT _val int DEFAULT null
)
	LANGUAGE plpgsql AS
$proc$
BEGIN
	_val := 1;
	for _ in 1.._power
	LOOP
		_val := _val * _num;
	END LOOP;
END;
$proc$