---
name: unknown_workflow_video_upscale_latent_upscale_68
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.954167
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyHunyuanVideo15Latent, HunyuanVideo15LatentUpscaleWithModel, HunyuanVideo15SuperResolution, KSamplerSelect, LatentUpscaleModelLoader, ModelSamplingSD3, PathchSageAttentionKJ, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2006663001679597569.json, 视频生成/文生视频/HUNYUAN 1.5 T2V 4步极速版_2073281127351144450.json, 视频生成/文生视频/HUNYUAN 1.5 T2V SR_2073280317422661634.json, 视频生成/文生视频/混元1.5T2V+超分-Aiwood_1992023623716368385.json, 视频生成/文生视频/混元1.5文生视频加速版720P_2005971109587668993.json, 视频生成/文生视频/混元1.5文生视频加速版720P_2016675572935565313.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_68

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2006663001679597569.json、视频生成/文生视频/HUNYUAN 1.5 T2V 4步极速版_2073281127351144450.json、视频生成/文生视频/HUNYUAN 1.5 T2V SR_2073280317422661634.json、视频生成/文生视频/混元1.5T2V+超分-Aiwood_1992023623716368385.json、视频生成/文生视频/混元1.5文生视频加速版720P_2005971109587668993.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyHunyuanVideo15Latent`
- `HunyuanVideo15LatentUpscaleWithModel`
- `HunyuanVideo15SuperResolution`
- `KSamplerSelect`
- `LatentUpscaleModelLoader`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `VAEDecodeTiled` —— 4/6 个有
- `CR Text` —— 3/6 个有
- `DF_Int_to_Float` —— 3/6 个有
- `JWInteger` —— 3/6 个有
- `MathExpression|pysssss` —— 3/6 个有
- `ImpactSwitch` —— 2/6 个有
- `VAEDecode` —— 2/6 个有
- `LoraLoader` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
