---
name: unknown_workflow_sampler_clip_vae_36
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.878167
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncodeFlux, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【遇见AI】FLUX Tools Redux多图参考_2041072547206275073.json, 图片生成/文生图/Nunchaku_Flux_12Lora_TurboVersion_v1_1914962492102012929.json, 图片生成/文生图/【遇见AI】FLUX1 GGUF版基础文生图_2039561392402993154.json, 图片生成/文生图/【遇见AI】FLUX1原版基础文生图_2039561375621582850.json, 图片生成/文生图/【遇见AI】FLUX版In-Context-LoRA，一致性_2041786416010629122.json, 图片生成/文生图/【遇见AI】flux1-krea-dev文生图基础_2047606141261189121.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_36

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/【遇见AI】FLUX Tools Redux多图参考_2041072547206275073.json、图片生成/文生图/Nunchaku_Flux_12Lora_TurboVersion_v1_1914962492102012929.json、图片生成/文生图/【遇见AI】FLUX1 GGUF版基础文生图_2039561392402993154.json、图片生成/文生图/【遇见AI】FLUX1原版基础文生图_2039561375621582850.json、图片生成/文生图/【遇见AI】FLUX版In-Context-LoRA，一致性_2041786416010629122.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncodeFlux`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingFlux` —— 4/6 个有
- `LoadImage` —— 3/6 个有
- `UnetLoaderGGUF` —— 3/6 个有
- `UNETLoader` —— 2/6 个有
- `CLIPVisionLoader` —— 1/6 个有
- `LoraLoader` —— 1/6 个有
- `NunchakuFluxDiTLoader` —— 1/6 个有
- `NunchakuFluxLoraLoader` —— 1/6 个有
- `ReduxAdvanced` —— 1/6 个有
- `StyleModelLoader` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 720 - 1472 | 6 | 79% |
| 高度 | 1024 | 1024 - 1280 | 6 | 91% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 720 - 1472，6 个样本
- 高度 中位数 1024，观测区间 1024 - 1280，6 个样本，取值集中（一致性 91%）
