---
name: unknown_workflow_lora_sampler_clip_204
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.91225
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/FLUX模型向日葵女孩人像摄影_1843904836679979009.json, 平台全量/Flux 文生图加放大，一键生成4K高清大图_1828817531984596993.json, 平台全量/一键生成奥特曼搞笑类型图片_1862023683601793026.json, 平台全量/指尖宠物_1837049358796701697.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_204

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/FLUX模型向日葵女孩人像摄影_1843904836679979009.json、平台全量/Flux 文生图加放大，一键生成4K高清大图_1828817531984596993.json、平台全量/一键生成奥特曼搞笑类型图片_1862023683601793026.json、平台全量/指尖宠物_1837049358796701697.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR SDXL Aspect Ratio` —— 3/4 个有
- `ModelSamplingFlux` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `Joy_caption` —— 2/4 个有
- `Joy_caption_load` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `EmptyLatentImage` —— 1/4 个有
- `ImageUpscaleWithModel` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `String Literal` —— 1/4 个有
- `UpscaleModelLoader` —— 1/4 个有
- `easy promptConcat` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | - | 1 | 100% |
| 高度 | 1280 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
