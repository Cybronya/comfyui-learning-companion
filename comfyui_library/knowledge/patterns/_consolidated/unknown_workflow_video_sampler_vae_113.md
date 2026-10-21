---
name: unknown_workflow_video_sampler_vae_113
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9412
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/1932675120529821697.json, 视频生成/文生视频/1932781560670081026.json, 视频生成/文生视频/1922872818927812610.json, 视频生成/文生视频/1925183972802764801.json, 视频生成/文生视频/1924303085684838402.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_113

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/1932675120529821697.json、视频生成/文生视频/1932781560670081026.json、视频生成/文生视频/1922872818927812610.json、视频生成/文生视频/1925183972802764801.json、视频生成/文生视频/1924303085684838402.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `JWInteger` —— 4/5 个有
- `WanVideoTeaCache` —— 3/5 个有
- `WanVideoVACEEncode` —— 3/5 个有
- `WanVideoVACEModelSelect` —— 3/5 个有
- `JjkText` —— 2/5 个有
- `WanVideoEmptyEmbeds` —— 2/5 个有
- `WanVideoLoraSelect` —— 2/5 个有
- `CR Prompt Text` —— 1/5 个有
- `FluxResolutionNode` —— 1/5 个有
- `Int` —— 1/5 个有
- `RH_Prompter` —— 1/5 个有
- `TextCombinerTwo` —— 1/5 个有
- `TextInput_` —— 1/5 个有
- `easy int` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
