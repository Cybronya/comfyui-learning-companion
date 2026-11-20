---
name: unknown_workflow_sampler_clip_vae_27
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.858667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, JjkText, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/文生图 ｜ 3D动漫玩偶三视图_1933875714414268417.json, 图片生成/文生图/Flux文生图-基础版_1889856882952089601.json, 图片生成/文生图/Flux模型 电商展台三维渲染效果_1826079381268639745.json, 图片生成/文生图/一键气球文字效果_2036273645370216450.json, 图片生成/文生图/一键气球文字效果_2037774758560931841.json, 平台全量/一键气球文字效果_1852185727315451906.json, 平台全量/像素风格插画_1867049186352136194.json, 平台全量/儿童绘本风格插画_1866404421067239425.json, 平台全量/双十一电商主题设计_1851889664369016834.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_27

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/文生图 ｜ 3D动漫玩偶三视图_1933875714414268417.json、图片生成/文生图/Flux文生图-基础版_1889856882952089601.json、图片生成/文生图/Flux模型 电商展台三维渲染效果_1826079381268639745.json、图片生成/文生图/一键气球文字效果_2036273645370216450.json、图片生成/文生图/一键气球文字效果_2037774758560931841.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `JjkText`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 8/9 个有
- `PreviewImage` —— 8/9 个有
- `Label (rgthree)` —— 7/9 个有
- `ImageUpscaleWithModel` —— 6/9 个有
- `UNETLoader` —— 6/9 个有
- `UpscaleModelLoader` —— 6/9 个有
- `VAEEncode` —— 5/9 个有
- `CheckpointLoaderSimple` —— 4/9 个有
- `FluxGuidance` —— 4/9 个有
- `FluxResolutionNode` —— 4/9 个有
- `Int Literal` —— 4/9 个有
- `LoraLoader` —— 4/9 个有
- `LoraLoaderModelOnly` —— 4/9 个有
- `ModelSamplingFlux` —— 4/9 个有
- `TextCombinerTwo` —— 3/9 个有
- `BRIA_RMBG_ModelLoader_Zho` —— 1/9 个有
- `BRIA_RMBG_Zho` —— 1/9 个有
- `Image Overlay` —— 1/9 个有
- `ImagePadForOutpaint` —— 1/9 个有
- `KSampler` —— 1/9 个有
- `LayerColor: ColorBalance` —— 1/9 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/9 个有
- `LoadImage` —— 1/9 个有
- `SDXLEmptyLatentSizePicker+` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1.075 | 0.75 - 1.2 | 4 | 83% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 832 | 512 - 1024 | 8 | 81% |
| 高度 | 1216 | 1 - 1280 | 9 | 58% |
| 采样步数 | 20 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 1 | 100% |
| 采样算法 | euler_ancestral | - | 1 | 100% |
| 调度器 | normal | - | 1 | 100% |
| 重绘幅度 | 0.45 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1.075，观测区间 0.75 - 1.2，4 个样本，取值集中（一致性 83%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 832，观测区间 512 - 1024，8 个样本，取值集中（一致性 81%）
- 高度 中位数 1216，观测区间 1 - 1280，9 个样本
