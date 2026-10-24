---
name: unknown_workflow_video_lora_sampler_439
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9818
common_nodes: [CLIPVisionLoader, ImageResizeKJv2, Int, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/wan图生视频+运镜=艾橘溪_1948677616428548098.json, 视频生成/图生视频/首尾帧=FusionX=图生视频=艾橘溪_1912904491438669825.json, 视频生成/图生视频/首尾帧=FusionX=图生视频_2041339598445481985.json, 视频生成/图生视频/首尾帧=FusionX=图生视频_2046408331203452929.json, 视频生成/图生视频/首尾帧Wan2.1高质量图生视频_1938975650491650049.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_439

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/wan图生视频+运镜=艾橘溪_1948677616428548098.json、视频生成/图生视频/首尾帧=FusionX=图生视频=艾橘溪_1912904491438669825.json、视频生成/图生视频/首尾帧=FusionX=图生视频_2041339598445481985.json、视频生成/图生视频/首尾帧=FusionX=图生视频_2046408331203452929.json、视频生成/图生视频/首尾帧Wan2.1高质量图生视频_1938975650491650049.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 4/5 个有
- `WanVideoEnhanceAVideo` —— 4/5 个有
- `WanVideoSLG` —— 4/5 个有
- `WanVideoTorchCompileSettings` —— 4/5 个有
- `Bjornulf_ShowInt` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有
- `WanVideoEncode` —— 1/5 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/5 个有
- `WanVideoUni3C_embeds` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
