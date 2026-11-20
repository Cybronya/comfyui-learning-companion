---
name: unknown_workflow_sampler_unet_vae_93
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.954083
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, TextEncodeQwenImageEditPlus_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/文字渲染-千问Edit2509图像编辑_1970818656336834562.json, 图片生成/文生图/服装迁移-千问_1986355660625477633.json, 平台全量/3D转绘-Qwen-Image-Edit图像编辑_1970843150505938945.json, 平台全量/Qwen Edit 产品换背景_1987887480714235905.json, 平台全量/Qwen edit plus controlnet控制工作流_1971191325901148162.json, 平台全量/Qwen edit plus 多图编辑工作流_1971194545465675777.json, 平台全量/服装迁移-千问Edit2509图像编辑_1970482734567223297.json, 平台全量/服装迁移-千问Edit2509图像编辑_1970788316364873730.json, 平台全量/服装迁移-千问_1986320654196756481.json, 平台全量/证件照-千问Edit2509图像编辑_1970531763221131266.json, 平台全量/证件照-千问Edit2509图像编辑_1970810713545580546.json, 平台全量/阮旭东AIGC：Qwen-Edit-Plus（Qwen_2509）超强多图编辑合成工作流_1971359707300577282.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_93

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/文字渲染-千问Edit2509图像编辑_1970818656336834562.json、图片生成/文生图/服装迁移-千问_1986355660625477633.json、平台全量/3D转绘-Qwen-Image-Edit图像编辑_1970843150505938945.json、平台全量/Qwen Edit 产品换背景_1987887480714235905.json、平台全量/Qwen edit plus controlnet控制工作流_1971191325901148162.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 10/12 个有
- `ImageStitch` —— 9/12 个有
- `Text Multiline` —— 6/12 个有
- `CFGNorm` —— 4/12 个有
- `ModelSamplingAuraFlow` —— 4/12 个有
- `PrimitiveInt` —— 4/12 个有
- `PrimitiveStringMultiline` —— 3/12 个有
- `AIO_Preprocessor` —— 1/12 个有
- `easy imageRemBg` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 6 - 20 | 12 | 71% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 12 | 69% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | beta57 | - | 12 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 6 - 20，12 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，12 个样本
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 beta57，12 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
