---
name: unknown_workflow_sampler_clip_checkpoint_14
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.835
common_nodes: [CLIPTextEncodeSDXL, CheckpointLoaderSimple, EmptyLatentImage, KSamplerAdvanced, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/250523_作业案例_（SDXL双采样）双模型文生图_工作流_1925579019461283841.json, 图片生成/文生图/SDXL完整官方工作流_2042144146009366530.json, 图片生成/文生图/SDXL模型精细工作流（满血版+refiner）文生图_1964348804235411457.json, 图片生成/文生图/SDXL模型风格化工作流（满血版+refiner）_1964382898122014721.json, 图片生成/文生图/sdxl标准工作流_2039947963614629889.json, 图片生成/文生图/【AI小王子】18.XL风格预设节点包_2046833312118870017.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_14

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/250523_作业案例_（SDXL双采样）双模型文生图_工作流_1925579019461283841.json、图片生成/文生图/SDXL完整官方工作流_2042144146009366530.json、图片生成/文生图/SDXL模型精细工作流（满血版+refiner）文生图_1964348804235411457.json、图片生成/文生图/SDXL模型风格化工作流（满血版+refiner）_1964382898122014721.json、图片生成/文生图/sdxl标准工作流_2039947963614629889.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncodeSDXL`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncodeSDXLRefiner` —— 5/6 个有
- `PreviewImage` —— 4/6 个有
- `SDXLPromptStylerAdvanced` —— 3/6 个有
- `Label (rgthree)` —— 2/6 个有
- `MathExpression|pysssss` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 6 | 83% |
| Prompt 约束强度(CFG) | 30 | 20 - 40 | 6 | 81% |
| 采样算法 | 8 | 8 - 8 | 6 | 100% |
| 调度器 | dpmpp_2m | - | 6 | 50% |
| 重绘幅度 | karras | - | 6 | 50% |
| 宽度 | 1024 | 1024 - 1024 | 6 | 100% |
| 高度 | 1024 | 1024 - 1024 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，6 个样本，一致性 83%
- Prompt 约束强度(CFG) 中位数 30，观测区间 20 - 40，6 个样本，取值集中（一致性 81%）
- 采样算法 中位数 8，观测区间 8 - 8，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_2m，6 个样本，一致性 50%
- 重绘幅度 最常用 karras，6 个样本，一致性 50%
- 宽度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 40，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
