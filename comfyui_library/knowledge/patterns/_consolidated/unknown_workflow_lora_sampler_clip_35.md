---
name: unknown_workflow_lora_sampler_clip_35
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8153
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/In-Context-LoRA-一致性人像摄影_1908846681855504386.json, 图片生成/文生图/In-Context-LoRA-电影分镜_1908549630693679105.json, 图片生成/文生图/In-Context-Lora _ 电影分镜头_1908700798354599938.json, 图片生成/文生图/In-Context-Lora人像摄影一致性_1943617599785607170.json, 图片生成/文生图/Nunchaku｜Flux 文生图 约2秒一张图_1988974782064496641.json, 图片生成/文生图/flux 1 + lora 文生图基础工作流_1937778776556376066.json, 图片生成/文生图/人物一致性，电影分镜一致性_1925132068681150465.json, 图片生成/文生图/极简Airbnb风3d图标生成器_1937774839442903042.json, 图片生成/文生图/生成无Ai感的美女写真_1929441410473431042.json, 图片生成/文生图/苹果毛玻璃图标设计器_1930927750276644866.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_35

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/In-Context-LoRA-一致性人像摄影_1908846681855504386.json、图片生成/文生图/In-Context-LoRA-电影分镜_1908549630693679105.json、图片生成/文生图/In-Context-Lora _ 电影分镜头_1908700798354599938.json、图片生成/文生图/In-Context-Lora人像摄影一致性_1943617599785607170.json、图片生成/文生图/Nunchaku｜Flux 文生图 约2秒一张图_1988974782064496641.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 9/10 个有
- `FluxGuidance` —— 5/10 个有
- `PreviewImage` —— 5/10 个有
- `easy imageSplitGrid` —— 5/10 个有
- `easy imagesSplitImage` —— 5/10 个有
- `JjkText` —— 4/10 个有
- `Text Concatenate (JPS)` —— 3/10 个有
- `CR Text` —— 1/10 个有
- `JjkConcat` —— 1/10 个有
- `NunchakuFluxDiTLoader` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1024 - 2048 | 10 | 68% |
| 高度 | 1116 | 1024 - 1728 | 10 | 77% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 1024 - 2048，10 个样本
- 高度 中位数 1116，观测区间 1024 - 1728，10 个样本
