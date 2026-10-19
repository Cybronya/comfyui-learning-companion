---
name: unknown_workflow_sampler_vae_34
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9242
common_nodes: [BasicGuider, BasicScheduler, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: [Text Multiline, CR Text]
members: [图片生成/文生图/1982707861027471361.json, 图片生成/文生图/1982900132742070274.json, 图片生成/文生图/1988974782064496641.json, 图片生成/文生图/生成系列性服装设计_1884234765942538241.json, 图片生成/文生图/风后文生图_1878760414459932673.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_34

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1982707861027471361.json、图片生成/文生图/1982900132742070274.json、图片生成/文生图/1988974782064496641.json、图片生成/文生图/生成系列性服装设计_1884234765942538241.json、图片生成/文生图/风后文生图_1878760414459932673.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
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
- `CLIPTextEncode` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `FluxGuidance` —— 2/5 个有
- `NunchakuFluxDiTLoader` —— 2/5 个有
- `BatchPromptSchedule` —— 1/5 个有
- `CR Text` —— 1/5 个有
- `DetailDaemonSamplerNode` —— 1/5 个有
- `Text Multiline` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 896 - 1080 | 5 | 94% |
| 高度 | 1152 | 720 - 1920 | 5 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 896 - 1080，5 个样本，取值集中（一致性 94%）
- 高度 中位数 1152，观测区间 720 - 1920，5 个样本
- 这些节点还没有知识卡，系统对它们的理解有限：Text Multiline、CR Text
