---
name: unknown_workflow_sampler_clip_unet_43
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.930824
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/FLUX 2 文生图_1993689182549770241.json, 图片生成/文生图/FLUX 3 高质量文生图_2114203882040680450.json, 图片生成/文生图/FLUX.2-Klein多模态文生图工作流_2068581821109071873.json, 图片生成/文生图/FLUX.2-Klein文生图工作流_2015679953211232258.json, 图片生成/文生图/FLUX.2-文生图工作流-支持中文输入_1993696439157063682.json, 图片生成/文生图/FLUX.2万物生成高质感_2069427067028074497.json, 图片生成/文生图/FLUX3 Image Klein 文生图_2111346567927123970.json, 图片生成/文生图/FLUX3 Image Klein 文生图（修复版·中文繁体招牌王）_2111323705954623489.json, 图片生成/文生图/Flux 2 txt2img 2K Image Generation_2037040628390957058.json, 图片生成/文生图/Flux 3_Image_Klein开源版-文生图_2111064999098671105.json, 图片生成/文生图/Flux2-4步文生图_2007026656766074882.json, 图片生成/文生图/Flux2文生图工作流_1993542491129446401.json, 图片生成/文生图/KOOK-MOSS-SFT-观澜_2112403091164319745.json, 图片生成/文生图/MOSS IMAGE 文生图_2113649019552624641.json, 图片生成/文生图/MOSS Text-to-Image 2K Turbo Edition 图生图2K极速版_2113063260466536449.json, 图片生成/文生图/MOSS优化版-文生图工作流_2113902662948311042.json, 图片生成/文生图/自动词优化Moss-image Sft fixed文生图-低显存版_2112824054842486786.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_43

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/文生图/FLUX 2 文生图_1993689182549770241.json、图片生成/文生图/FLUX 3 高质量文生图_2114203882040680450.json、图片生成/文生图/FLUX.2-Klein多模态文生图工作流_2068581821109071873.json、图片生成/文生图/FLUX.2-Klein文生图工作流_2015679953211232258.json、图片生成/文生图/FLUX.2-文生图工作流-支持中文输入_1993696439157063682.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 9/17 个有
- `LoraLoaderModelOnly` —— 6/17 个有
- `PrimitiveStringMultiline` —— 6/17 个有
- `ConditioningZeroOut` —— 5/17 个有
- `FluxGuidance` —— 5/17 个有
- `LoadImage` —— 3/17 个有
- `SkipLayerGuidanceDiTSimple` —— 3/17 个有
- `PreviewAny` —— 2/17 个有
- `PreviewImage` —— 1/17 个有
- `RH_LLMAPI_Pro_Node` —— 1/17 个有
- `TextGenerate` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16 | 6 - 25 | 17 | 58% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 17 | 43% |
| 采样算法 | euler | - | 17 | 71% |
| 调度器 | simple | - | 17 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 16，观测区间 6 - 25，17 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，17 个样本，取值分散，一致性仅 43%
- 采样算法 最常用 euler，17 个样本，一致性 71%
- 调度器 最常用 simple，17 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
