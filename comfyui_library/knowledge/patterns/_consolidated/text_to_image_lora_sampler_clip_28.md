---
name: text_to_image_lora_sampler_clip_28
type: Text To Image
frequency: 22
level: strong
coverage: 0.781227
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1文生图处理生成工具_2102563638816104449.json, 图片生成/图生图/Qwen Image 2.1最强开源图像编辑多图模特换装图生图处理工具_2102088091476512769.json, 图片生成/图生图/Qwen Image 2.1生图及编辑工作流，支持12张参考图一致性最强开源方案_2107154350245240833.json, 图片生成/图生图/Qwen Image 2.1生图改图拼图三合一，多参考高精度可控图生图方案_2103257263350829057.json, 图片生成/图生图/Qwen Image 2.1电商换装神器｜模特服装自动替换一键完成_2103671470185603074.json, 图片生成/图生图/Qwen Image 2.1空间折叠流万法编辑，多图编辑抠图文生图全功能合一_2103569010649559042.json, 图片生成/图生图/Qwen Image 2.1自动分镜短剧分镜生成，图生图快速产出故事板_2102850796370096129.json, 图片生成/图生图/Qwen Image 2.1自动分镜短剧分镜生成，图生图快速产出故事板_2103270132993847297.json, 图片生成/图生图/Qwen Image 2.1自动分镜短剧分镜生成，支持三视图参考的图生图工作流_2102897765192916994.json, 图片生成/图生图/Qwen Image 2.1角色资产四视图极速版，4步8步加速图生图方案_2103944948725927937.json, 图片生成/图生图/Qwen Image 2.1透明背景抠图，PNG通道输出图生图专用工作流_2102867983600283649.json, 图片生成/图生图/Qwen image 2.1图片编辑 局部修改指令式操作_2105111897447157762.json, 图片生成/图生图/Qwen image 2.1图片编辑多面手｜图片换背景其它处理全包｜图生图顺手_2102252322154962946.json, 图片生成/图生图/Qwen image 2.1图片编辑，海报制作场景特效全能_2112335625205669889.json, 图片生成/图生图/Qwen image 2.1多图编辑int8版｜自带提示词增强｜图生图低显存友好_2102210466104832001.json, 图片生成/图生图/Qwen image 2.1多图编辑｜图生图多参考融合｜改图精准不跑偏_2104827606054035458.json, 图片生成/图生图/Qwen-Image-2.1图像编辑10张参考图｜局部重绘换装 图生图全能_2104094197203685378.json, 图片生成/图生图/Qwen-Image-2.1图像编辑｜最多10张参考图图生图随心改_2106230157538324481.json, 图片生成/图生图/QwenImage2.1 I2I官方提示词助手｜图生图有帮手｜描述写不好也能改图_2102637170602364929.json, 图片生成/图生图/QwenImage2.1图片编辑加提示词助手｜局部重绘超顺手_2103087888484356098.json, 图片生成/图生图/QwenImage2.1图生图搭配官方提示词助手，I2I编辑效率大幅提升_2102838137943838722.json, 视频生成/图生视频/QwenImage2.1图生图搭配官方提示词助手，I2I编辑效率大幅提升_2105866245517168642.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_28

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1文生图处理生成工具_2102563638816104449.json、图片生成/图生图/Qwen Image 2.1最强开源图像编辑多图模特换装图生图处理工具_2102088091476512769.json、图片生成/图生图/Qwen Image 2.1生图及编辑工作流，支持12张参考图一致性最强开源方案_2107154350245240833.json、图片生成/图生图/Qwen Image 2.1生图改图拼图三合一，多参考高精度可控图生图方案_2103257263350829057.json、图片生成/图生图/Qwen Image 2.1电商换装神器｜模特服装自动替换一键完成_2103671470185603074.json…）

- **类型**：Text To Image
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 22 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 21/22 个有
- `孤海注释` —— 21/22 个有
- `ComfySwitchNode` —— 20/22 个有
- `QwenImage21Cache` —— 20/22 个有
- `ResolutionSelector` —— 20/22 个有
- `SaveImageAdvanced` —— 15/22 个有
- `PrimitiveStringMultiline` —— 12/22 个有
- `easy showAnything` —— 10/22 个有
- `GetNode` —— 9/22 个有
- `SetNode` —— 9/22 个有
- `BatchImagesNode` —— 8/22 个有
- `TextGenerateLTX2Prompt` —— 8/22 个有
- `Fast Groups Bypasser (rgthree)` —— 7/22 个有
- `Any Switch (rgthree)` —— 4/22 个有
- `ImageBatchMulti` —— 4/22 个有
- `ImageConcatMulti` —— 4/22 个有
- `ImageScaleToTotalPixels` —— 4/22 个有
- `JsonExtractString` —— 4/22 个有
- `TextConcatenator` —— 4/22 个有
- `TextGenerate` —— 4/22 个有
- `PreviewImage` —— 3/22 个有
- `PrimitiveBoolean` —— 1/22 个有
- `Text` —— 1/22 个有
- `TextCombinerTwo` —— 1/22 个有
- `easy cleanGpuUsed` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 22 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 22 | 100% |
| 采样算法 | er_sde | - | 22 | 100% |
| 调度器 | beta | - | 22 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 22 | 100% |
| 宽度 | 80 | 80 - 80 | 22 | 100% |
| 高度 | 80 | 80 - 80 | 22 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 25/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，22 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，22 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，22 个样本，一致性 100%
- 调度器 最常用 beta，22 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，22 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，22 个样本，取值集中（一致性 100%）
- 高发问题（25/22 个样本）：Steps较低可能导致细节不足
