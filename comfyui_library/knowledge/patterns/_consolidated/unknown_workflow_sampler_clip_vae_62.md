---
name: unknown_workflow_sampler_clip_vae_62
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.908333
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CR Prompt Text, EmptyLatentImage, KSamplerSelect, NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/🦖新王HiDream洗图Fast模式对比工作流_1911706061030551553.json, 图片生成/文生图/NunChaku加速版SillyTavern带Lora生图工作流_1922302399132684289.json, "图片生成/文生图/吊打Flux,新王HiDream洗图Fast模式对比工作流_1910667121410437122.json"]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_62

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/🦖新王HiDream洗图Fast模式对比工作流_1911706061030551553.json、图片生成/文生图/NunChaku加速版SillyTavern带Lora生图工作流_1922302399132684289.json、图片生成/文生图/吊打Flux,新王HiDream洗图Fast模式对比工作流_1910667121410437122.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyLatentImage`
- `KSamplerSelect`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `HiDreamSampler` —— 2/3 个有
- `ImageConcanate` —— 2/3 个有
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `Note Plus (mtb)` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `easy promptConcat` —— 2/3 个有
- `CR Combine Prompt` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
