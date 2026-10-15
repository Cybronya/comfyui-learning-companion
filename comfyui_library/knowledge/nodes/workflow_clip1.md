# workflow/clip1

## 节点类型

`workflow/clip1`

## 分类

Conditioning

## 作用

CLIP/条件相关节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `CLIP:CLIP`（1 次）
- `DeepTranslatorCLIPTextEncodeNode clip:CLIP`（1 次）

## 输出

- `条件:CONDITIONING`（1 次）
- `字符串:STRING`（1 次）
- `DeepTranslatorCLIPTextEncodeNode 条件:CONDITIONING`（1 次）
- `DeepTranslatorCLIPTextEncodeNode 字符串:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["auto", "english", "disable", "", "", "GoogleTranslator", "森林风景照片，高清晰度，真实光照，丁达尔效应，安塞尔亚当斯参与了这个项目，徕卡1600mm f/5.6长焦镜头，8k，r`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
