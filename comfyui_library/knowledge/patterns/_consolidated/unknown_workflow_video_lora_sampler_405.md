---
name: unknown_workflow_video_lora_sampler_405
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9082
common_nodes: [CR Prompt Text, JWInteger, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoFreeInitArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy int]
problems: []
missing: []
members: [视频生成/图生视频/1945815960743800834.json, 视频生成/图生视频/1947158911092305922.json, 视频生成/图生视频/1945677633763909634.json, 视频生成/图生视频/1945637624423882753.json, 视频生成/文生视频/1945683257658888194.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_405

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1945815960743800834.json、视频生成/图生视频/1947158911092305922.json、视频生成/图生视频/1945677633763909634.json、视频生成/图生视频/1945637624423882753.json、视频生成/文生视频/1945683257658888194.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CR Prompt Text`
- `JWInteger`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoFreeInitArgs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJ` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `SimpleMath+` —— 4/5 个有
- `WanVideoImageToVideoEncode` —— 4/5 个有
- `ImageConcanate` —— 1/5 个有
- `RH_Translator` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有
- `WanVideoEmptyEmbeds` —— 1/5 个有
- `WanVideoEncode` —— 1/5 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/5 个有
- `WanVideoUni3C_embeds` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
