---
name: unknown_workflow_lora_sampler_clip_19
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.826357
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, LoraLoaderModelOnly, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Labubu（拉布布）生成器_1935575269891559426.json, 图片生成/文生图/Nunchaku-flux2秒极速文生图_1909968900275273729.json, 图片生成/文生图/Nunchaku-flux2秒极速文生图_2042435095121891330.json, 图片生成/文生图/Nunchaku-flux2秒极速文生图_2047558509369233409.json, 图片生成/文生图/SVDQ和官方FLUX对比_1910633207707172866.json, 图片生成/文生图/hidream_全系出图与FLUX对比_1917844166154321921.json, 图片生成/文生图/天才樱木花道_1925124635254267905.json, 图片生成/文生图/太乙真人工作流_1929399159059595265.json, 图片生成/文生图/汉服美女工生成作流_1931186440095641601.json, 图片生成/文生图/灌篮高手-三井寿_1926264181538910210.json, 图片生成/文生图/灌篮高手-宫城良田_1926262954042290178.json, 图片生成/文生图/灌篮高手-流川枫_1925427219194163201.json, 图片生成/文生图/灌篮高手-赤木刚宪_1926115550580338689.json, 图片生成/文生图/越前龙马工作流_1933821200713830402.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_19

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/Labubu（拉布布）生成器_1935575269891559426.json、图片生成/文生图/Nunchaku-flux2秒极速文生图_1909968900275273729.json、图片生成/文生图/Nunchaku-flux2秒极速文生图_2042435095121891330.json、图片生成/文生图/Nunchaku-flux2秒极速文生图_2047558509369233409.json、图片生成/文生图/SVDQ和官方FLUX对比_1910633207707172866.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 10/14 个有
- `JoinStrings` —— 9/14 个有
- `PrimitiveString` —— 9/14 个有
- `Text Multiline` —— 9/14 个有
- `easy hiresFix` —— 9/14 个有
- `CR Text` —— 4/14 个有
- `NunchakuFluxDiTLoader` —— 4/14 个有
- `NunchakuFluxLoraLoader` —— 4/14 个有
- `NunchakuTextEncoderLoader` —— 4/14 个有
- `Note Plus (mtb)` —— 2/14 个有
- `SDXLEmptyLatentSizePicker+` —— 2/14 个有
- `KSampler` —— 1/14 个有
- `ModelSamplingSD3` —— 1/14 个有
- `QuadrupleCLIPLoader` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024x1024 (1.0) | - | 2 | 100% |
| 高度 | 1 | - | 2 | 100% |
| 采样步数 | 28 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | lcm | - | 1 | 100% |
| 调度器 | normal | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 最常用 1024x1024 (1.0)，2 个样本，一致性 100%
- 高度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
