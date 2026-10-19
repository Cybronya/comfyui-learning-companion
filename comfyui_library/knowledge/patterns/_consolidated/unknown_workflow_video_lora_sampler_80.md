---
name: unknown_workflow_video_lora_sampler_80
type: Unknown Workflow
frequency: 17
level: strong
coverage: 0.839706
common_nodes: [BerniniStudio, CLIPLoader, GetNode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2078439441877790721.json, 视频生成/图生视频/2065400514141048833.json, 视频生成/图生视频/2081577097444810753.json, 视频生成/图生视频/2075050205141094402.json, 视频生成/图生视频/2074045202817437698.json, 视频生成/图生视频/2073577575993139202.json, 视频生成/图生视频/2074795916221050881.json, 视频生成/图生视频/2063147705244930049.json, 视频生成/图生视频/2064931292038385665.json, 视频生成/图生视频/调试Bernini Studio工作流-4步lora_rv2v_2102665904747270146.json, 视频生成/图生视频/2073745061728313345.json, 视频生成/图生视频/2073682935554854913.json, 视频生成/图生视频/2082366639907102721.json, 视频生成/图生视频/2082437380983844866.json, 视频生成/图生视频/2082454463452893186.json, 视频生成/图生视频/2082456967376883713.json, 视频生成/图生视频/2074035799124955138.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_80

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/2078439441877790721.json、视频生成/图生视频/2065400514141048833.json、视频生成/图生视频/2081577097444810753.json、视频生成/图生视频/2075050205141094402.json、视频生成/图生视频/2074045202817437698.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 17 个 workflow 都包含：
- `BerniniStudio`
- `CLIPLoader`
- `GetNode`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `RTXVideoSuperResolution` —— 15/17 个有
- `VHS_LoadVideo` —— 15/17 个有
- `ImageConcatMulti` —— 14/17 个有
- `Int` —— 10/17 个有
- `SimpleMath+` —— 7/17 个有
- `VHS_VideoInfo` —— 2/17 个有
- `Any Switch (rgthree)` —— 1/17 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/17 个有
- `GIMMVFI_interpolate` —— 1/17 个有
- `LoadAudio` —— 1/17 个有
- `MathExpression|pysssss` —— 1/17 个有
- `ShowAnything|Mie` —— 1/17 个有
- `Text` —— 1/17 个有
- `easy showAnything` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 17 | 88% |
| Prompt 约束强度(CFG) | 4 | 4 - 8 | 17 | 78% |
| 采样算法 | 1 | 1 - 1 | 17 | 100% |
| 调度器 | euler | - | 17 | 100% |
| 重绘幅度 | simple | - | 17 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，17 个样本，一致性 88%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 8，17 个样本
- 采样算法 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，17 个样本，一致性 100%
- 重绘幅度 最常用 simple，17 个样本，一致性 100%
