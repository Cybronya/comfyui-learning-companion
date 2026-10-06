# workflow/clip

## 节点类型

`workflow/clip`

## 分类

Conditioning

## 作用

CLIP/条件相关节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `CLIP:CLIP`（2 次）
- `ref_image:IMAGE`（1 次）
- `DeepTranslatorCLIPTextEncodeNode clip:CLIP`（1 次）
- `DeepTranslatorCLIPTextEncodeNode 2 clip:CLIP`（1 次）
- `DeepTranslatorCLIPTextEncodeNode 3 clip:CLIP`（1 次）
- `DeepTranslatorCLIPTextEncodeNode 4 clip:CLIP`（1 次）

## 输出

- `字符串:STRING`（2 次）
- `条件:CONDITIONING`（2 次）
- `describe:STRING`（1 次）
- `DeepTranslatorCLIPTextEncodeNode 条件:CONDITIONING`（1 次）
- `DeepTranslatorCLIPTextEncodeNode 字符串:STRING`（1 次）
- `DeepTranslatorCLIPTextEncodeNode 2 条件:CONDITIONING`（1 次）
- `DeepTranslatorCLIPTextEncodeNode 2 字符串:STRING`（1 次）
- `DeepTranslatorCLIPTextEncodeNode 3 条件:CONDITIONING`（1 次）
- `DeepTranslatorCLIPTextEncodeNode 3 字符串:STRING`（1 次）
- `DeepTranslatorCLIPTextEncodeNode 4 条件:CONDITIONING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Line art,bold lines,cartoon, flat,Round eyes,cartoon image，the beautiful girl has a middle part with bangs, a bun hair`（1 次）
- `["auto", "english", "disable", "", "", "GoogleTranslator", "NSFW，低清晰度，模糊的，变形，扭曲，不符合常理的，", "auto", "english", "disable", `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
