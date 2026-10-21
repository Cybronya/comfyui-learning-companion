---
name: unknown_workflow_video_sampler_vae_28
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.736917
common_nodes: [FluxResolutionNode, Int, JWInteger, JjkText, LoadWanVideoT5TextEncoder, MathExpression|pysssss, RH_Captioner, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy showAnything]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/1932694201777672193.json, 视频生成/图生视频/2052305268150677505.json, 视频生成/图生视频/1922977171818598402.json, 视频生成/图生视频/1924455095239364609.json, 视频生成/图生视频/1972857610967928833.json, 视频生成/图生视频/2057436928223571969.json, 视频生成/图生视频/2047301907374415874.json, 视频生成/图生视频/2068063600496959490.json, 视频生成/图生视频/1947183216568754178.json, 视频生成/图生视频/1981756791207927809.json, 视频生成/文生视频/1922918246369083394.json, 视频生成/文生视频/1930813054726897666.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_28

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/1932694201777672193.json、视频生成/图生视频/2052305268150677505.json、视频生成/图生视频/1922977171818598402.json、视频生成/图生视频/1924455095239364609.json、视频生成/图生视频/1972857610967928833.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 12 个 workflow 都包含：
- `FluxResolutionNode`
- `Int`
- `JWInteger`
- `JjkText`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `RH_Captioner`
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
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Evaluate Integers` —— 11/12 个有
- `InversionDemoLazyIndexSwitch` —— 11/12 个有
- `MMAudioFeatureUtilsLoader` —— 11/12 个有
- `MMAudioModelLoader` —— 11/12 个有
- `MMAudioSampler` —— 11/12 个有
- `RH_Prompter` —— 11/12 个有
- `SaveAudio` —— 11/12 个有
- `TextCombinerTwo` —— 11/12 个有
- `AudioCombine` —— 10/12 个有
- `CLIPLoader` —— 10/12 个有
- `CLIPTextEncode` —— 10/12 个有
- `CheckpointLoaderSimple` —— 10/12 个有
- `ColorMatch` —— 10/12 个有
- `EmptyLatentAudio` —— 10/12 个有
- `ImageConcatMulti` —— 10/12 个有
- `ImageResize+` —— 10/12 个有
- `KSampler` —— 10/12 个有
- `LoadImage` —— 10/12 个有
- `RH_Translator` —— 10/12 个有
- `VAEDecodeAudio` —— 10/12 个有
- `PreviewAudio` —— 9/12 个有
- `PreviewImage` —— 9/12 个有
- `ImpactSwitch` —— 8/12 个有
- `Note _O` —— 8/12 个有
- `ImageFromBatch+` —— 2/12 个有
- `easy int` —— 2/12 个有
- `easy textSwitch` —— 2/12 个有
- `Label (rgthree)` —— 1/12 个有
- `RH_LLMAPI_NODE` —— 1/12 个有
- `easy anythingIndexSwitch` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 40 | 40 - 40 | 10 | 100% |
| 高度 | 1 | 1 - 1 | 10 | 100% |
| 采样步数 | 60 | 60 - 60 | 10 | 100% |
| Prompt 约束强度(CFG) | 7 | 7 - 7 | 10 | 100% |
| 采样算法 | dpmpp_3m_sde_gpu | - | 10 | 100% |
| 调度器 | exponential | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 10/12 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 宽度 中位数 40，观测区间 40 - 40，10 个样本，取值集中（一致性 100%）
- 高度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 60，观测区间 60 - 60，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 7 - 7，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_3m_sde_gpu，10 个样本，一致性 100%
- 调度器 最常用 exponential，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/12 个样本）：发现KSampler但没有VAEDecode
