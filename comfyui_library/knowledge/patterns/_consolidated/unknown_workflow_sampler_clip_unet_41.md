---
name: unknown_workflow_sampler_clip_unet_41
type: Unknown Workflow
frequency: 12
level: weak
coverage: 0.941
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1950475750447173633.json, 视频生成/图生视频/1968955228710133762.json, 视频生成/图生视频/1989350434903085058.json, 视频生成/图生视频/1952176106529083393.json, 视频生成/图生视频/1998363625523937282.json, 视频生成/图生视频/1997975012088905729.json, 视频生成/图生视频/2037349147073843201.json, 视频生成/图生视频/1962156046351536130.json, 视频生成/图生视频/1967772488862150657.json, 视频生成/图生视频/1994764866990878721.json, 视频生成/图生视频/1950181163430273026.json, 视频生成/图生视频/1984131896915492865.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_41

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/1950475750447173633.json、视频生成/图生视频/1968955228710133762.json、视频生成/图生视频/1989350434903085058.json、视频生成/图生视频/1952176106529083393.json、视频生成/图生视频/1998363625523937282.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 9/12 个有
- `LoraLoaderModelOnly` —— 9/12 个有
- `SaveVideo` —— 9/12 个有
- `WanImageToVideo` —— 8/12 个有
- `WanFirstLastFrameToVideo` —— 4/12 个有
- `LayerUtility: PurgeVRAM V2` —— 3/12 个有
- `VHS_VideoCombine` —— 3/12 个有
- `RH_LLMAPI_NODE` —— 1/12 个有
- `ShowText|pysssss` —— 1/12 个有
- `easy imageConcat` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 12 | 67% |
| Prompt 约束强度(CFG) | 8 | 4 - 20 | 12 | 35% |
| 采样算法 | 1.5 | 1 - 4 | 12 | 41% |
| 调度器 | euler | - | 12 | 100% |
| 重绘幅度 | simple | - | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，12 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 8，观测区间 4 - 20，12 个样本，取值分散，一致性仅 35%
- 采样算法 中位数 1.5，观测区间 1 - 4，12 个样本，取值分散，一致性仅 41%
- 调度器 最常用 euler，12 个样本，一致性 100%
- 重绘幅度 最常用 simple，12 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
