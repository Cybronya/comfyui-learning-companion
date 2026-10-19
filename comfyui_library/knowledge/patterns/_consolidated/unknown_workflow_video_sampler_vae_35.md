---
name: unknown_workflow_video_sampler_vae_35
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7136
common_nodes: [ApplyFaceProcessor, FaceProcessorLoader, LoadImage, VHS_VideoCombine, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1957474365233360898.json, 视频生成/图生视频/1956293638198362114.json, 视频生成/图生视频/1973164651716415490.json, 视频生成/文生视频/03-12-02-WAN2.1-参考人物视频转绘-Standin+Vace_1989933948379820033.json, 视频生成/文生视频/1957474365233360898.json, 视频生成/文生视频/1955702074303397890.json, 视频生成/文生视频/1955698165593751554.json, 视频生成/文生视频/1956763443317628929.json, 视频生成/文生视频/1957506592558215169.json, 视频生成/文生视频/1956266838781034498.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_35

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/1957474365233360898.json、视频生成/图生视频/1956293638198362114.json、视频生成/图生视频/1973164651716415490.json、视频生成/文生视频/03-12-02-WAN2.1-参考人物视频转绘-Standin+Vace_1989933948379820033.json、视频生成/文生视频/1957474365233360898.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 10 个 workflow 都包含：
- `ApplyFaceProcessor`
- `FaceProcessorLoader`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoAddStandInLatent`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadWanVideoT5TextEncoder` —— 8/10 个有
- `PreviewImage` —— 8/10 个有
- `WanVideoLoraSelect` —— 8/10 个有
- `WanVideoSetBlockSwap` —— 8/10 个有
- `WanVideoSetLoRAs` —— 8/10 个有
- `WanVideoTextEncode` —— 8/10 个有
- `WanVideoTorchCompileSettings` —— 8/10 个有
- `INTConstant` —— 7/10 个有
- `WanVideoEmptyEmbeds` —— 7/10 个有
- `GetNode` —— 6/10 个有
- `ImageResizeKJv2` —— 6/10 个有
- `SetNode` —— 6/10 个有
- `VHS_LoadVideo` —— 6/10 个有
- `WanVideoVACEEncode` —— 6/10 个有
- `OpenposePreprocessor` —— 5/10 个有
- `WanVideoVACEModelSelect` —— 5/10 个有
- `WanVideoVACEStartToEndFrame` —— 5/10 个有
- `easy imageRemBg` —— 5/10 个有
- `ImageConcanate` —— 4/10 个有
- `ImageConcatMulti` —— 4/10 个有
- `CR Text` —— 3/10 个有
- `ImpactInt` —— 2/10 个有
- `Label (rgthree)` —— 2/10 个有
- `WanVideoLoraSelectMulti` —— 2/10 个有
- `WanVideoTextEncodeCached` —— 2/10 个有
- `AIO_Preprocessor` —— 1/10 个有
- `ImpactSwitch` —— 1/10 个有
- `JWInteger` —— 1/10 个有
- `Note Plus (mtb)` —— 1/10 个有
- `SimpleMath+` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
