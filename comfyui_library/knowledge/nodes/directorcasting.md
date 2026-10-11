# DirectorCasting

## 节点类型

`DirectorCasting`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `prev_cast_dict:DICT`（3 次）
- `char1_img:IMAGE`（3 次）
- `char2_img:IMAGE`（3 次）
- `char3_img:IMAGE`（3 次）
- `char4_img:IMAGE`（3 次）
- `char5_img:IMAGE`（3 次）
- `char6_img:IMAGE`（3 次）
- `char1_name:STRING`（3 次）
- `char2_name:STRING`（3 次）
- `char3_name:STRING`（3 次）

## 输出

- `角色名册(Dict):DICT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["张元清", "女长辈", "", "", "", ""]`（2 次）
- `["西格玛", "鲛渊", "", "", "", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
