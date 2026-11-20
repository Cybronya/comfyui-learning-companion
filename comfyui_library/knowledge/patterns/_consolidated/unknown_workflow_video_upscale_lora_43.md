---
name: unknown_workflow_video_upscale_lora_43
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9395
common_nodes: [CR Text, CreateCFGScheduleFloatList, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, ImpactInt, LoadWanVideoT5TextEncoder, Seed (rgthree), SimpleMath+, UpscaleModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.2 文生视频 高动态高细节_1972686604550774785.json, 视频生成/文生视频/🐳Wan2.2 文生视频 高动态高细节 邪修增强版🐳_1972186550123556865.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_43

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/Wan2.2 文生视频 高动态高细节_1972686604550774785.json、视频生成/文生视频/🐳Wan2.2 文生视频 高动态高细节 邪修增强版🐳_1972186550123556865.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `CreateCFGScheduleFloatList`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `ImpactInt`
- `LoadWanVideoT5TextEncoder`
- `Seed (rgthree)`
- `SimpleMath+`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `ImageScaleToMegapixels` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `SetNode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
