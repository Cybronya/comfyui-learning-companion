---
name: unknown_workflow_sampler_clip_unet_36
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.811842
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/MOSS_Text-to-Image_2K_Turbo_Edition_图生图2K极速版_2113466135764099073.json, 图片生成/图生图/Moss-image-文生图（8步加速）_2112146425906814977.json, 图片生成/图生图/Moss-image-文生图（提示词增强）_2112140949404082178.json, 图片生成/图生图/moss文生图简易版_2116173584493273090.json, 图片生成/图生图/moss生图工作流_2115685657757700098.json, 图片生成/图生图/图片编辑_moss_2116491113925267457.json, 图片生成/文生图/MOSS优化版-文生图工作流_2113902662948311042.json, 图片生成/文生图/MOSS文生图 + LoRA支持_2114192252502372354.json, 图片生成/文生图/MOSS生图工作流_2115738552272252929.json, 图片生成/文生图/Moss Base+SFT 双模融合8步工作流_2115612079012007938.json, 图片生成/文生图/Moss base+sft模型融合方案_2116558531745902593.json, 图片生成/文生图/文生图_moss_2116460668621770754.json, 图片生成/文生图/网红MOSS文生图 + LoRA支持_2115978618118696962.json, 图片生成/文生图/自用文生图_2115313494429102082.json, 平台全量/万能图片复刻_2117445537992630273.json, 视频生成/图生视频/图片编辑_moss_2116711198682075138.json, 视频生成/图生视频/图片编辑_moss_2116725998912892930.json, 视频生成/文生视频/MOSS_sft_Comfyui官方_2113787365826326529.json, 视频生成/文生视频/MOSS_sft_Comfyui官方_2113788793810673665.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_36

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/MOSS_Text-to-Image_2K_Turbo_Edition_图生图2K极速版_2113466135764099073.json、图片生成/图生图/Moss-image-文生图（8步加速）_2112146425906814977.json、图片生成/图生图/Moss-image-文生图（提示词增强）_2112140949404082178.json、图片生成/图生图/moss文生图简易版_2116173584493273090.json、图片生成/图生图/moss生图工作流_2115685657757700098.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 17/19 个有
- `SkipLayerGuidanceDiTSimple` —— 16/19 个有
- `PreviewAny` —— 15/19 个有
- `LoraLoaderModelOnly` —— 13/19 个有
- `TextGenerate` —— 10/19 个有
- `PreviewImage` —— 7/19 个有
- `RH_LLMAPI_Pro_Node` —— 7/19 个有
- `EmptyImage` —— 5/19 个有
- `LoadImage` —— 5/19 个有
- `MOSSMergePreset` —— 4/19 个有
- `CR Prompt Text` —— 2/19 个有
- `WujiUpscaler2` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 50 | 19 | 54% |
| Prompt 约束强度(CFG) | 3 | 1 - 3.5 | 19 | 73% |
| 采样算法 | er_sde | - | 19 | 63% |
| 调度器 | simple | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 50，19 个样本
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 3.5，19 个样本
- 采样算法 最常用 er_sde，19 个样本，一致性 63%
- 调度器 最常用 simple，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
