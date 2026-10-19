---
name: unknown_workflow_video_sampler_vae_81
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.679667
common_nodes: [CR Text, GetNode, ImpactSwitch, LoadWanVideoT5TextEncoder, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: [CR Text, CR Text Concatenate]
members: [图片生成/文生图/1934081139910823938.json, 视频生成/文生视频/1934086264885043201.json, 视频生成/文生视频/1924067062367645697.json, 视频生成/文生视频/1924084830865453057.json, 视频生成/文生视频/1933687634323791874.json, 视频生成/文生视频/1945827090790838274.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_81

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1934081139910823938.json、视频生成/文生视频/1934086264885043201.json、视频生成/文生视频/1924067062367645697.json、视频生成/文生视频/1924084830865453057.json、视频生成/文生视频/1933687634323791874.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 6 个 workflow 都包含：
- `CR Text`
- `GetNode`
- `ImpactSwitch`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `JWInteger` —— 5/6 个有
- `MathExpression|pysssss` —— 5/6 个有
- `RH_LLMAPI_NODE` —— 5/6 个有
- `easy showAnything` —— 5/6 个有
- `WanVideoApplyNAG` —— 3/6 个有
- `WanVideoTextEncode` —— 3/6 个有
- `WanVideoTextEncodeSingle` —— 3/6 个有
- `WanVideoVACEEncode` —— 3/6 个有
- `FluxResolutionNode` —— 2/6 个有
- `CR Text Concatenate` —— 1/6 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/6 个有
- `GIMMVFI_interpolate` —— 1/6 个有
- `ImageScaleToMegapixels` —— 1/6 个有
- `RH_Prompter` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `UpscaleModelLoader` —— 1/6 个有
- `WanVideoFreeInitArgs` —— 1/6 个有
- `WanVideoLoraSelect` —— 1/6 个有
- `WanVideoTeaCache` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR Text Concatenate
