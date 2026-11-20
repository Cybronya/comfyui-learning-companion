---
name: unknown_workflow_sampler_vae_70
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6695
common_nodes: [DualCLIPLoader, DyPE_Condition, DyPE_Encode, DyPE_KSampler, DyPE_Model, ImpactSwitch, JWInteger, LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, PreviewImage, RH_Translator, SaveImage, ShowText|pysssss, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/【 DyPE 】 FLUX - Krea  2 - 4 K 高清直出，文生图 + 图片反推_1984807816806481922.json, 图片生成/文生图/【 DyPE 】 FLUX - SRPO  2 - 4 K 高清直出 文生图 + 图片反推_1987345787942277122.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_70

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/【 DyPE 】 FLUX - Krea  2 - 4 K 高清直出，文生图 + 图片反推_1984807816806481922.json、图片生成/文生图/【 DyPE 】 FLUX - SRPO  2 - 4 K 高清直出 文生图 + 图片反推_1987345787942277122.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 2 个 workflow 都包含：
- `DualCLIPLoader`
- `DyPE_Condition`
- `DyPE_Encode`
- `DyPE_KSampler`
- `DyPE_Model`
- `ImpactSwitch`
- `JWInteger`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LoadImage`
- `PreviewImage`
- `RH_Translator`
- `SaveImage`
- `ShowText|pysssss`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `DyPE_FLUX` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `FluxGuidance` —— 1/2 个有
- `KSampler` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `UNETLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | res_2s | - | 1 | 100% |
| 调度器 | beta57 | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
