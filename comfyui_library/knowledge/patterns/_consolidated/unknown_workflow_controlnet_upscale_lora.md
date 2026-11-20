---
name: unknown_workflow_controlnet_upscale_lora
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.944778
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, GetImageSize, ImageScaleToTotalPixels, ImageUpscaleWithModel, LoraLoaderModelOnly, ModelPatchLoader, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Z-image Controlnet Uion 2.1优化高级采样_2010904466274390017.json, 图片生成/图生图/Z-image+Controlnet视频首帧姿势控制生图_2001265449847451649.json, 图片生成/图生图/Z-image秒变MOE模型，Controlnet和lora和谐共生_1996950295303360513.json, 图片生成/图生图/视频首帧动态控制生图_2002426719292276738.json, 图片生成/文生图/Z-image Controlnet Uion 2.1 线稿控制_2005605888377450497.json, 图片生成/文生图/Z-image+Controlnet视频首帧动态控制生图_2000971709572317185.json, 图片生成/文生图/Z-image+control_2001795995862220802.json, 平台全量/空白工作流_2014510445310255106.json, 平台全量/🦖N版Z-image 姿势模仿（灰度解码）_2000395078889766914.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_lora

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Z-image Controlnet Uion 2.1优化高级采样_2010904466274390017.json、图片生成/图生图/Z-image+Controlnet视频首帧姿势控制生图_2001265449847451649.json、图片生成/图生图/Z-image秒变MOE模型，Controlnet和lora和谐共生_1996950295303360513.json、图片生成/图生图/视频首帧动态控制生图_2002426719292276738.json、图片生成/文生图/Z-image Controlnet Uion 2.1 线稿控制_2005605888377450497.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 9 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 8/9 个有
- `KSamplerAdvanced` —— 8/9 个有
- `INTConstant` —— 7/9 个有
- `Seed (rgthree)` —— 7/9 个有
- `LoadImage` —— 6/9 个有
- `GetImageRangeFromBatch` —— 3/9 个有
- `VHS_LoadVideo` —— 3/9 个有
- `AILab_QwenVL` —— 2/9 个有
- `Image Comparer (rgthree)` —— 2/9 个有
- `ttN concat` —— 2/9 个有
- `Display Any (rgthree)` —— 1/9 个有
- `ImageScaleBy` —— 1/9 个有
- `Int` —— 1/9 个有
- `KSampler (Efficient)` —— 1/9 个有
- `PreviewAny` —— 1/9 个有
- `TT_img_enc` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 9 | 100% |
| 高度 | 1536 | 1536 - 1536 | 9 | 100% |
| 采样步数 | randomize | - | 9 | 78% |
| Prompt 约束强度(CFG) | 10 | 2 - 10 | 9 | 72% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | euler | - | 9 | 89% |
| 重绘幅度 | simple | - | 9 | 89% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，9 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，9 个样本，取值集中（一致性 100%）
- 采样步数 最常用 randomize，9 个样本，一致性 78%
- Prompt 约束强度(CFG) 中位数 10，观测区间 2 - 10，9 个样本
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，9 个样本，一致性 89%
- 重绘幅度 最常用 simple，9 个样本，一致性 89%
