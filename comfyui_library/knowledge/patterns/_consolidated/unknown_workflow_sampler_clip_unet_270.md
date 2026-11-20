---
name: unknown_workflow_sampler_clip_unet_270
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.900333
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/For循环批量提示词跑图_1948523697077387265.json, 图片生成/文生图/【一键运行】二次元性感美少女_2018845332670521345.json, 图片生成/文生图/【一键运行】牛皮革皮质纹理增强生成器_1936219766145323010.json, 图片生成/文生图/批量提示词跑图_1947936412476801026.json, 平台全量/Workflow 15 (Text - Flux)_1866021242246479874.json, 平台全量/【一键运行】超写实科幻神话电影大片风格渲染_2057341653987446786.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_270

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/For循环批量提示词跑图_1948523697077387265.json、图片生成/文生图/【一键运行】二次元性感美少女_2018845332670521345.json、图片生成/文生图/【一键运行】牛皮革皮质纹理增强生成器_1936219766145323010.json、图片生成/文生图/批量提示词跑图_1947936412476801026.json、平台全量/Workflow 15 (Text - Flux)_1866021242246479874.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/6 个有
- `String Literal` —— 3/6 个有
- `easy seed` —— 3/6 个有
- `DeepTranslatorTextNode` —— 2/6 个有
- `LoadImageMask` —— 2/6 个有
- `Text` —— 2/6 个有
- `Text Load Line From File` —— 2/6 个有
- `easy forLoopEnd` —— 2/6 个有
- `easy forLoopStart` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1080 | 6 | 89% |
| 高度 | 1024 | 1024 - 1552 | 6 | 79% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1080，6 个样本，取值集中（一致性 89%）
- 高度 中位数 1024，观测区间 1024 - 1552，6 个样本
