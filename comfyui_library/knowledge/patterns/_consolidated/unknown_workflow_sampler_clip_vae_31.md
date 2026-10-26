---
name: unknown_workflow_sampler_clip_vae_31
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.966429
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/CFGzero简单工作流带lora_1928999965027155970.json, 图片生成/文生图/FLUX文生图 繁花lora工作流_1942505597264924674.json, 图片生成/文生图/Flux 1 文生图基础工作流_1937783580867084290.json, 图片生成/文生图/Flux+Lora标准文生图_1932966165364834305.json, 图片生成/文生图/Flux文生图工作流_1941002485245100033.json, 图片生成/文生图/沙雕动画场景{中文提示词输入开跑版}_1934978430360592385.json, 图片生成/文生图/沙雕动画场景专用工作流_2075008312994787329.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_31

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/CFGzero简单工作流带lora_1928999965027155970.json、图片生成/文生图/FLUX文生图 繁花lora工作流_1942505597264924674.json、图片生成/文生图/Flux 1 文生图基础工作流_1937783580867084290.json、图片生成/文生图/Flux+Lora标准文生图_1932966165364834305.json、图片生成/文生图/Flux文生图工作流_1941002485245100033.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 6/7 个有
- `UNETLoader` —— 6/7 个有
- `DeepTranslatorTextNode` —— 4/7 个有
- `CR Text` —— 3/7 个有
- `ImageScaleBy` —— 3/7 个有
- `ImageUpscaleWithModel` —— 3/7 个有
- `UpscaleModelLoader` —— 3/7 个有
- `FluxSampler` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `ShowText|pysssss` —— 2/7 个有
- `VAEEncode` —— 2/7 个有
- `ttN concat` —— 2/7 个有
- `CFGZeroStar` —— 1/7 个有
- `FluxGuidance` —— 1/7 个有
- `ImageSmartSharpen+` —— 1/7 个有
- `Int` —— 1/7 个有
- `Note Plus (mtb)` —— 1/7 个有
- `TextInputBasic` —— 1/7 个有
- `UnetLoaderGGUF` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1152 | 1024 - 1440 | 7 | 87% |
| 高度 | 1024 | 768 - 1536 | 7 | 70% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1152，观测区间 1024 - 1440，7 个样本，取值集中（一致性 87%）
- 高度 中位数 1024，观测区间 768 - 1536，7 个样本
