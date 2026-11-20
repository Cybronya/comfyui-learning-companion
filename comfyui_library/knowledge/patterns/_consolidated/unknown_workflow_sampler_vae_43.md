---
name: unknown_workflow_sampler_vae_43
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.89975
common_nodes: [BasicGuider, BasicScheduler, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【遇见AI】FLUX Tools Redux多图参考_2041072547206275073.json, 图片生成/文生图/Nunchaku_Flux_12Lora_TurboVersion_v1_1914962492102012929.json, 图片生成/文生图/【遇见AI】FLUX1 GGUF版基础文生图_2039561392402993154.json, 图片生成/文生图/【遇见AI】FLUX1原版基础文生图_2039561375621582850.json, 图片生成/文生图/【遇见AI】FLUX版In-Context-LoRA，一致性_2041786416010629122.json, 图片生成/文生图/【遇见AI】flux1-krea-dev文生图基础_2047606141261189121.json, 平台全量/全能图片G-4o风格卡通IP形象一致性表情包_2007359849683750914.json, 平台全量/图像融合丨产品融合_1931329024453181441.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_43

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/【遇见AI】FLUX Tools Redux多图参考_2041072547206275073.json、图片生成/文生图/Nunchaku_Flux_12Lora_TurboVersion_v1_1914962492102012929.json、图片生成/文生图/【遇见AI】FLUX1 GGUF版基础文生图_2039561392402993154.json、图片生成/文生图/【遇见AI】FLUX1原版基础文生图_2039561375621582850.json、图片生成/文生图/【遇见AI】FLUX版In-Context-LoRA，一致性_2041786416010629122.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncodeFlux` —— 7/8 个有
- `LoadImage` —— 4/8 个有
- `ModelSamplingFlux` —— 4/8 个有
- `UNETLoader` —— 3/8 个有
- `UnetLoaderGGUF` —— 3/8 个有
- `CLIPVisionLoader` —— 2/8 个有
- `LoraLoader` —— 2/8 个有
- `NunchakuFluxDiTLoader` —— 2/8 个有
- `ReduxAdvanced` —— 2/8 个有
- `StyleModelLoader` —— 2/8 个有
- `CLIPTextEncode` —— 1/8 个有
- `FluxGuidance` —— 1/8 个有
- `NunchakuFluxLoraLoader` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 720 - 1472 | 8 | 79% |
| 高度 | 1024 | 1024 - 1280 | 8 | 92% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 720 - 1472，8 个样本
- 高度 中位数 1024，观测区间 1024 - 1280，8 个样本，取值集中（一致性 92%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
