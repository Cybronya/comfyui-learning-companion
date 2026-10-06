# LayerUtility: ImageScaleByAspectRatio V2

## 节点类型

`LayerUtility: ImageScaleByAspectRatio V2`

## 分类

Image Processing（LayerStyle 系列自定义节点）

## 作用

把输入图片按目标宽高比缩放/裁切/加边，常放在图生图链路最前端，
把任意尺寸的参考图整理成模型期望的输入比例。

## 参数（统计自 404 个真实 workflow，220 次出现）

| 参数 | 说明 | 实测分布 |
|---|---|---|
| aspect_ratio | 目标比例 | 92% 为 original（跟随原图） |
| proportional_width/height | 比例倍数 | 多为 1 |
| fit_method | 适配方式 | letterbox（补边）为主，crop（裁切）次之 |
| method | 插值算法 | lanczos 为主，bilinear 少量 |
| divisible_by | 尺寸取整步长 | 8 最常见（latent 要求被 8 整除），部分为 None |
| longest_side | 长边目标像素 | 1536 居多，其次 1280 / 1920 / 1024 |
| background_color | 补边底色 | `#000000` |

## 常见问题与风险

- divisible_by 必须设 8（或 16），否则 latent 尺寸非法直接报错。
- letterbox 会带入黑边，重绘类任务黑边会被模型当成内容画进去；
  要求满幅时用 crop。

## 可信度

Generated（2026-10-06，参数分布实测，letterbox/crop 行为为通行语义）TODO(待验证)
