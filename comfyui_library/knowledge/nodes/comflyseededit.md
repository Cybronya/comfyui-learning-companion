# ComflySeededit

## 节点类型

`ComflySeededit`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `prompt:STRING`（2 次）
- `scale:FLOAT`（1 次）
- `seed:INT`（1 次）
- `api_key:STRING`（1 次）
- `add_logo:BOOLEAN`（1 次）
- `logo_position:COMBO`（1 次）
- `logo_language:COMBO`（1 次）
- `logo_text:STRING`（1 次）

## 输出

- `edited_image:IMAGE`（2 次）
- `response:STRING`（2 次）
- `image_url:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["让女孩闭上眼睛", 0.5, 1629039260, "randomize", "sk-KaRChWAYKP0t8eX6E483032f08Af4a84AfDe32Ba97373e9a", false, "右下角", "中文", ""]`（1 次）
- `["让女孩闭上眼睛", 0.5, 814074915, "randomize", "", false, "右下角", "中文", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
