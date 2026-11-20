---
name: unknown_workflow_video_lora_sampler_802
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.45
common_nodes: [GIMMVFI_interpolate, GetNode, LoadWanVideoT5TextEncoder, PrimitiveInt, RIFE VFI, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoSetRadialAttention, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/03-03-02-WAN2.1-视频转绘-t2v-kijai_1989235364458016770.json, 视频生成/图生视频/03-02-02-WAN2.1-图生视频-kijai_1989234021240549377.json, 视频生成/文生视频/03-01-02-WAN2.1-文生视频-kijai_1989233864696541185.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_802

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/03-03-02-WAN2.1-视频转绘-t2v-kijai_1989235364458016770.json、视频生成/图生视频/03-02-02-WAN2.1-图生视频-kijai_1989234021240549377.json、视频生成/文生视频/03-01-02-WAN2.1-文生视频-kijai_1989233864696541185.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：45%

## 共有节点

全部 3 个 workflow 都包含：
- `GIMMVFI_interpolate`
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveInt`
- `RIFE VFI`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoSetRadialAttention`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJ` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `WanVideoEmptyEmbeds` —— 2/3 个有
- `Anything Everywhere3` —— 1/3 个有
- `CLIPVisionLoader` —— 1/3 个有
- `CR Prompt Text` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有
- `WanVideoClipVisionEncode` —— 1/3 个有
- `WanVideoEncode` —— 1/3 个有
- `WanVideoImageToVideoEncode` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
