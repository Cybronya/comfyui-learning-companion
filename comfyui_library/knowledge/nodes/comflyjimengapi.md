# ComflyJimengApi

## 节点类型

`ComflyJimengApi`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `prompt:STRING`（1 次）
- `scale:FLOAT`（1 次）
- `seed:INT`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `api_key:STRING`（1 次）
- `use_pre_llm:BOOLEAN`（1 次）
- `add_logo:BOOLEAN`（1 次）
- `logo_position:COMBO`（1 次）

## 输出

- `generated_image:IMAGE`（1 次）
- `response:STRING`（1 次）
- `image_url:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 2.5, 1727090512, "randomize", 1328, 1328, "", false, false, "右下角", "中文", "", 0.3, ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
