---
name: unknown_workflow_sampler_clip_unet_362
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.807
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/MiniMax H3：文本生图_2115634578835730433.json, 图片生成/文生图/pipi-anima高级采样器工作流_2078243608947412994.json, 图片生成/文生图/文生图V2_2087151483677659138.json, 平台全量/minimax_h3文生图V2版_2118133750608515073.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_362

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/MiniMax H3：文本生图_2115634578835730433.json、图片生成/文生图/pipi-anima高级采样器工作流_2078243608947412994.json、图片生成/文生图/文生图V2_2087151483677659138.json、平台全量/minimax_h3文生图V2版_2118133750608515073.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 2/4 个有
- `LTXVSeparateAVLatent` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `ModelAttentionBackend` —— 2/4 个有
- `ResolutionSelector` —— 2/4 个有
- `FluxGuidance` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `LoraLoader` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `SetNode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 864 - 1080 | 4 | 92% |
| 高度 | 1232 | 1024 - 1920 | 4 | 73% |
| LoRA 模型强度 | 0 | - | 1 | 100% |
| LoRA 文本强度 | 0 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 864 - 1080，4 个样本，取值集中（一致性 92%）
- 高度 中位数 1232，观测区间 1024 - 1920，4 个样本
