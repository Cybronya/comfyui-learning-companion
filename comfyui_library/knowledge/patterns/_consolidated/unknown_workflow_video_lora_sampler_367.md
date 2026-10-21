---
name: unknown_workflow_video_lora_sampler_367
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.901333
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1948953733947371521.json, 视频生成/图生视频/1949101004231979010.json, 视频生成/图生视频/1946509129076891649.json, 视频生成/图生视频/1947243498794815490.json, 视频生成/文生视频/1947564947329982466.json, 视频生成/文生视频/1948615375945641985.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_367

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1948953733947371521.json、视频生成/图生视频/1949101004231979010.json、视频生成/图生视频/1946509129076891649.json、视频生成/图生视频/1947243498794815490.json、视频生成/文生视频/1947564947329982466.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoSetRadialAttention` —— 5/6 个有
- `ImageResizeKJv2` —— 4/6 个有
- `SimpleMath+` —— 3/6 个有
- `TextInput_` —— 3/6 个有
- `WanVideoTorchCompileSettings` —— 3/6 个有
- `ImageResizeKJ` —— 2/6 个有
- `Seed (rgthree)` —— 2/6 个有
- `easy int` —— 2/6 个有
- `CR Text` —— 1/6 个有
- `ttN int` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
