---
name: unknown_workflow_video_sampler_vae_110
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8244
common_nodes: [JWInteger, JjkText, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/VACE 14B-图生视频+自动提示词_1923028261134397442.json, 视频生成/文生视频/VACE 14B-9步超级加速文生视频(全自动扩写提示词)_1923557148746240001.json, 视频生成/文生视频/【完美高质量】Wan2.1 VACE 14B-可自定时长图生视频_1929380593648439297.json, 视频生成/文生视频/【文生视频】可换lora wan2.1 I2V 14Bi2v美女走路背影_1929785774303252482.json, 视频生成/文生视频/核爆炸VACE 14B-3-9步超级加速文生视频(全自动扩写提示词)_1924303085684838402.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_110

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/VACE 14B-图生视频+自动提示词_1923028261134397442.json、视频生成/文生视频/VACE 14B-9步超级加速文生视频(全自动扩写提示词)_1923557148746240001.json、视频生成/文生视频/【完美高质量】Wan2.1 VACE 14B-可自定时长图生视频_1929380593648439297.json、视频生成/文生视频/【文生视频】可换lora wan2.1 I2V 14Bi2v美女走路背影_1929785774303252482.json、视频生成/文生视频/核爆炸VACE 14B-3-9步超级加速文生视频(全自动扩写提示词)_1924303085684838402.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
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
- `easy showAnything` —— 4/5 个有
- `FluxResolutionNode` —— 3/5 个有
- `Int` —— 3/5 个有
- `MathExpression|pysssss` —— 3/5 个有
- `RH_Prompter` —— 3/5 个有
- `TextCombinerTwo` —— 3/5 个有
- `WanVideoLoraSelect` —— 3/5 个有
- `easy int` —— 3/5 个有
- `ImageResize+` —— 2/5 个有
- `InversionDemoLazyIndexSwitch` —— 2/5 个有
- `LoadImage` —— 2/5 个有
- `ColorMatch` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `ImageFromBatch+` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有
- `easy textSwitch` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
