# RH_LLMAPI_NODE

## 节点类型

`RH_LLMAPI_NODE`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 7 个 workflow 中。

## 输入

- `ref_image:IMAGE`（7 次）
- `video:VIDEO`（7 次）
- `ref_image1:IMAGE`（7 次）
- `ref_image2:IMAGE`（7 次）
- `ref_image3:IMAGE`（7 次）
- `api_baseurl:STRING`（7 次）
- `api_key:STRING`（7 次）
- `model:STRING`（7 次）
- `role:STRING`（7 次）
- `prompt:STRING`（7 次）

## 输出

- `describe:STRING`（7 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", "", "You are a professional AI image generation prompt engineer. You shall strictly follow the requirements bel`（2 次）
- `["", "", "", "【输入方式】：参考图 + 文本描述  \n【延展目标】：基于上一张图的画面风格、人物外形、光影氛围、镜头语言，生成下一张分镜图，使得剧情延续\n\n保持人物外观一致  \n色调光影与参考图统一  \n背景元素延续`（2 次）
- `["", "", "", "", "", 0.6, 1522669183, "randomize"]`（1 次）
- `["", "", "", "", "", 0.6, 1846863797, "randomize"]`（1 次）
- `["", "", "", "You are a helpful assistant", "Hello", 0.6, 2054861611, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
