---
name: unknown_workflow_video_sampler_vae_124
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.82675
common_nodes: [JWInteger, JjkText, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1923028261134397442.json, 视频生成/文生视频/1923557148746240001.json, 视频生成/文生视频/1929380593648439297.json, 视频生成/文生视频/1929785774303252482.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_124

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1923028261134397442.json、视频生成/文生视频/1923557148746240001.json、视频生成/文生视频/1929380593648439297.json、视频生成/文生视频/1929785774303252482.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `JWInteger`
- `JjkText`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxResolutionNode` —— 3/4 个有
- `Int` —— 3/4 个有
- `MathExpression|pysssss` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `ImageResize+` —— 2/4 个有
- `InversionDemoLazyIndexSwitch` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `RH_Prompter` —— 2/4 个有
- `TextCombinerTwo` —— 2/4 个有
- `WanVideoLoraSelect` —— 2/4 个有
- `easy int` —— 2/4 个有
- `ColorMatch` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `ImageFromBatch+` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有
- `easy textSwitch` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
