---
name: unknown_workflow_controlnet_clip_unet
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.781
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, LoadImage, ModelPatchLoader, ModelSamplingAuraFlow, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Mesh2Motion首帧生成参考图_2052926077273681922.json, 图片生成/图生图/Qwen-inpaint 局部重绘=艾橘溪_1959188827518742529.json, 图片生成/图生图/z-image-turbo_fun_controlnet_v2.0_1996424354097414146.json, 图片生成/图生图/z-image-turbo_图生图姿态控制_2048304144070479873.json, 图片生成/文生图/AA--Zimage参考文生图-controlnet-人物姿势_建筑构图等-基础_2006739441741733890.json, 图片生成/文生图/AA--批量洗图-Zimage controlnet精准洗图_生图+4K放大--批量版本_2005623741910581250.json, 图片生成/文生图/AA--洗图-Zimage controlnet精准自动洗图_生图+4K放大--单图版本_2001512031041798146.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_clip_unet

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Mesh2Motion首帧生成参考图_2052926077273681922.json、图片生成/图生图/Qwen-inpaint 局部重绘=艾橘溪_1959188827518742529.json、图片生成/图生图/z-image-turbo_fun_controlnet_v2.0_1996424354097414146.json、图片生成/图生图/z-image-turbo_图生图姿态控制_2048304144070479873.json、图片生成/文生图/AA--Zimage参考文生图-controlnet-人物姿势_建筑构图等-基础_2006739441741733890.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `LoadImage`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 6/7 个有
- `AIO_Preprocessor` —— 5/7 个有
- `ConditioningZeroOut` —— 5/7 个有
- `ImageScaleToTotalPixels` —— 5/7 个有
- `GetImageSize` —— 4/7 个有
- `KSampler` —— 4/7 个有
- `Fast Groups Bypasser (rgthree)` —— 3/7 个有
- `INTConstant` —— 3/7 个有
- `KSamplerAdvanced` —— 3/7 个有
- `LayerUtility: PurgeVRAM` —— 3/7 个有
- `SeedVR2LoadDiTModel` —— 3/7 个有
- `SeedVR2LoadVAEModel` —— 3/7 个有
- `SeedVR2VideoUpscaler` —— 3/7 个有
- `Qwen3_VQA` —— 2/7 个有
- `easy saveText` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
- `Bjornulf_ShowInt` —— 1/7 个有
- `DJZImageScaleToTotalPixels` —— 1/7 个有
- `DWPreprocessor` —— 1/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `Int` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `RHBatchImages:` —— 1/7 个有
- `RHExtractImage` —— 1/7 个有
- `RHUploadZip` —— 1/7 个有
- `easy forLoopEnd` —— 1/7 个有
- `easy forLoopStart` —— 1/7 个有
- `easy imageCount` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 4 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 20 | 7 | 0% |
| 采样算法 | dpmpp_2m_sde | - | 7 | 43% |
| 调度器 | sgm_uniform | - | 7 | 43% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，4 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 20，7 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 dpmpp_2m_sde，7 个样本，一致性 43%
- 调度器 最常用 sgm_uniform，7 个样本，一致性 43%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
