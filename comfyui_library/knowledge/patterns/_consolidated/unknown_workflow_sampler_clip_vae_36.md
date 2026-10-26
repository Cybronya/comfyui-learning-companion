---
name: unknown_workflow_sampler_clip_vae_36
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.952286
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncodeFlux, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/【遇见AI】nunchaku版FLUX1基础文生图_2047228635328811010.json, 图片生成/文生图/根据提示词生成图片_2058844453082845186.json, 图片生成/文生图/根据提示词生成图片_2058847096706519041.json, 图片生成/文生图/毛绒奇幻国·Zhiban_1880497829063061506.json, 图片生成/文生图/毛绒奇幻国·Zhiban_1880529226179964930.json, 图片生成/文生图/游戏Icon-奖励宝箱一键生成_1980191535377584130.json, 图片生成/文生图/精品高清手办套装3D哪吒甲亢哥盲盒玩具玩偶_1911771666933055489.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_36

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/【遇见AI】nunchaku版FLUX1基础文生图_2047228635328811010.json、图片生成/文生图/根据提示词生成图片_2058844453082845186.json、图片生成/文生图/根据提示词生成图片_2058847096706519041.json、图片生成/文生图/毛绒奇幻国·Zhiban_1880497829063061506.json、图片生成/文生图/毛绒奇幻国·Zhiban_1880529226179964930.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncodeFlux`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 6/7 个有
- `UNETLoader` —— 6/7 个有
- `LoraLoader` —— 4/7 个有
- `LoadImage` —— 1/7 个有
- `ModelSamplingFlux` —— 1/7 个有
- `NunchakuFluxDiTLoader` —— 1/7 个有
- `NunchakuTextEncoderLoaderV2` —— 1/7 个有
- `RH_Translator` —— 1/7 个有
- `SeargePromptCombiner` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 832 - 2000 | 7 | 64% |
| 高度 | 1024 | 1024 - 1248 | 7 | 93% |
| LoRA 模型强度 | 1 | 0.8 - 1 | 4 | 91% |
| LoRA 文本强度 | 1 | 1 - 3.5 | 4 | 33% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 832 - 2000，7 个样本
- 高度 中位数 1024，观测区间 1024 - 1248，7 个样本，取值集中（一致性 93%）
- LoRA 模型强度 中位数 1，观测区间 0.8 - 1，4 个样本，取值集中（一致性 91%）
- LoRA 文本强度 中位数 1，观测区间 1 - 3.5，4 个样本，取值分散，一致性仅 33%
