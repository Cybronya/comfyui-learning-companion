---
name: unknown_workflow_video_sampler_vae_175
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.726
common_nodes: [ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, RMBG, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoModelLoader, WanVideoPhantomEmbeds, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy int]
problems: []
missing: []
members: [视频生成/图生视频/2018210609103380482.json, 视频生成/图生视频/2017750442649853954.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_175

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2018210609103380482.json、视频生成/图生视频/2017750442649853954.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `RMBG`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoModelLoader`
- `WanVideoPhantomEmbeds`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `DF_Int_to_Float` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `Text` —— 1/2 个有
- `intToFloat _O` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
