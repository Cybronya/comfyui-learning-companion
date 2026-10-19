---
name: text_to_image_lora_sampler_clip_96
type: Text To Image
frequency: 9
level: strong
coverage: 0.884444
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/去AI感增强真实感工作流，MiniMax H3 LTX Wan图生视频动作迁移多合一_2103189879533424642.json, 图片生成/文生图/图生图任意角度转换双图版｜Qwen Image2.1 多角度出图更立体_2105540395974348802.json, 图片生成/文生图/平替全能图片G图像编辑 Qwen Image 2.1生图加编辑12张参考图_2104300055376261122.json, 数字人/数字人/千问大模型驱动的数字人工作流，多功能AI生成方案_2102883846000828418.json, 数字人/数字人/千问大模型驱动的数字人工作流，多功能AI生成方案_2105115732848766978.json, 视频生成/图生视频/Qwen Image 2.1参考人物姿势，图生视频姿势参考生成方案_2103578331991068673.json, 视频生成/图生视频/Qwen_Image_2.1_PE图像编辑工作流，人像写真图生图其它图片处理方案_2109526005462421506.json, 视频生成/图生视频/Qwen_Image_2.1透明背景抠图，PNG通道输出图生图专用工作流_2105508227860492289.json, 视频生成/图生视频/Remove模型Qwen_Image_2.1_PE姿势编辑工作流，人物类特效擦除图生图_2108739961490071554.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_96

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/去AI感增强真实感工作流，MiniMax H3 LTX Wan图生视频动作迁移多合一_2103189879533424642.json、图片生成/文生图/图生图任意角度转换双图版｜Qwen Image2.1 多角度出图更立体_2105540395974348802.json、图片生成/文生图/平替全能图片G图像编辑 Qwen Image 2.1生图加编辑12张参考图_2104300055376261122.json、数字人/数字人/千问大模型驱动的数字人工作流，多功能AI生成方案_2102883846000828418.json、数字人/数字人/千问大模型驱动的数字人工作流，多功能AI生成方案_2105115732848766978.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 8/9 个有
- `QwenImage21Cache` —— 8/9 个有
- `TextEncodeQwenImage21` —— 8/9 个有
- `ComfySwitchNode` —— 7/9 个有
- `ResolutionSelector` —— 7/9 个有
- `EmptyImage` —— 5/9 个有
- `PreviewImage` —— 5/9 个有
- `孤海注释` —— 5/9 个有
- `easy cleanGpuUsed` —— 4/9 个有
- `easy showAnything` —— 4/9 个有
- `CR Prompt Text` —— 3/9 个有
- `QwenPERewriteT8` —— 3/9 个有
- `CR Text` —— 2/9 个有
- `QwenImage21BlockCacheT8` —— 2/9 个有
- `QwenImage21SageAttentionT8` —— 2/9 个有
- `QwenImage21SpectrumT8` —— 2/9 个有
- `SaveImageAdvanced` —— 2/9 个有
- `AIO_Preprocessor` —— 1/9 个有
- `ImageConcatMulti` —— 1/9 个有
- `RHHiddenNodes` —— 1/9 个有
- `TextCombinerTwo` —— 1/9 个有
- `VHS_LoadVideo` —— 1/9 个有
- `VHS_VideoCombine` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
