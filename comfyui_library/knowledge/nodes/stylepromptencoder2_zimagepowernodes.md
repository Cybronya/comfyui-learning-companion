# StylePromptEncoder2 //ZImagePowerNodes

## 节点类型

`StylePromptEncoder2 //ZImagePowerNodes`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `clip:CLIP`（1 次）
- `customization:STRING`（1 次）
- `text:STRING`（1 次）

## 输出

- `CONDITIONING:CONDITIONING`（1 次）
- `STRING:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["\"Holographic Device\"", null, null, "在暮色四合的画舫上，一位身着粉紫纱裙的女子倚栏而坐，裙摆轻扬，足踝交叠，左手轻握茶盏，右手轻抚额前发丝，眼神低垂，似在沉思；镜头采用中近景俯拍，聚焦于她微露的胸`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
