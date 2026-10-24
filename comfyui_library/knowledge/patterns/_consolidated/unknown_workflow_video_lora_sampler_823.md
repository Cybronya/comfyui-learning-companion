---
name: unknown_workflow_video_lora_sampler_823
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.901
common_nodes: [LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoEasyCache, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/aniwan制作可爱二次元表情包_1949733818894295041.json, 视频生成/图生视频/二次元动漫视频生成（Wan_lightX2V）_1949706641991192577.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_823

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/aniwan制作可爱二次元表情包_1949733818894295041.json、视频生成/图生视频/二次元动漫视频生成（Wan_lightX2V）_1949706641991192577.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEasyCache`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `WanVideoEnhanceAVideo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
