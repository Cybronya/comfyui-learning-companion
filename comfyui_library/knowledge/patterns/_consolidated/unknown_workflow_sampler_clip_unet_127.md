---
name: unknown_workflow_sampler_clip_unet_127
type: Unknown Workflow
frequency: 9
level: weak
coverage: 0.638333
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, Int, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/反推提示词/26ttovrefine_2049450102586089473.json, 图片生成/图生图/WAN2.2-LightX2V-I2V超强动态（邪修）_2002515455887720450.json, 图片生成/图生图/WAN2.2-LightX2V-I2V（图生视频）_1993593720855609346.json, 图片生成/图生图/WAN2.2-RemixV2-I2V_2002500408180371457.json, 视频生成/图生视频/004.Wan视频之源001.超强动态高遵循度图生视频_2035278593374298113.json, 视频生成/图生视频/16.最强-超强动态，高质量，高遵循度_1992224912406368258.json, 视频生成/图生视频/DaSiWa-WAN2.2单图生视频_2033100146149433345.json, 视频生成/图生视频/Fisher大佬分享的DaSiWa单视频工作流-需要自己编写提示词-以便精准控制视频生成_2011699908318859265.json, 视频生成/图生视频/WAN2.2图生视频终极版_2083953699881316354.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_127

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/反推提示词/26ttovrefine_2049450102586089473.json、图片生成/图生图/WAN2.2-LightX2V-I2V超强动态（邪修）_2002515455887720450.json、图片生成/图生图/WAN2.2-LightX2V-I2V（图生视频）_1993593720855609346.json、图片生成/图生图/WAN2.2-RemixV2-I2V_2002500408180371457.json、视频生成/图生视频/004.Wan视频之源001.超强动态高遵循度图生视频_2035278593374298113.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `Int`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 8/9 个有
- `Fast Groups Bypasser (rgthree)` —— 7/9 个有
- `LoraLoaderModelOnly` —— 7/9 个有
- `RIFE VFI` —— 7/9 个有
- `WanImageToVideo` —— 7/9 个有
- `wanBlockSwap` —— 5/9 个有
- `CR Text` —— 2/9 个有
- `CreateVideo` —— 2/9 个有
- `GetImagesFromBatchIndexed` —— 2/9 个有
- `PainterI2V` —— 2/9 个有
- `SetNode` —— 2/9 个有
- `CompressImages` —— 1/9 个有
- `Fast Groups Muter (rgthree)` —— 1/9 个有
- `GetNode` —— 1/9 个有
- `ImageResizeKJv2` —— 1/9 个有
- `PreviewAny` —— 1/9 个有
- `RH_LLMAPI_NODE` —— 1/9 个有
- `RTXVideoSuperResolution` —— 1/9 个有
- `SaveVideo` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 9 | 78% |
| Prompt 约束强度(CFG) | 4 | 4 - 20 | 9 | 13% |
| 采样算法 | 1 | 1 - 1 | 9 | 100% |
| 调度器 | euler | - | 9 | 100% |
| 重绘幅度 | normal | - | 9 | 78% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，9 个样本，一致性 78%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 20，9 个样本，取值分散，一致性仅 13%
- 采样算法 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，9 个样本，一致性 100%
- 重绘幅度 最常用 normal，9 个样本，一致性 78%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
