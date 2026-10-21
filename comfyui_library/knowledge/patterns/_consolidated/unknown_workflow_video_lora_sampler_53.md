---
name: unknown_workflow_video_lora_sampler_53
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.8392
common_nodes: [BerniniStudio, CLIPLoader, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/文生图/Bernini studio自由切换提示词前缀_2064529633915269122.json, 视频生成/图生视频/2078439441877790721.json, 视频生成/图生视频/2073592310989942786.json, 视频生成/图生视频/2073584193665331202.json, 视频生成/图生视频/2065400514141048833.json, 视频生成/图生视频/2081577097444810753.json, 视频生成/图生视频/2075050205141094402.json, 视频生成/图生视频/2074045202817437698.json, 视频生成/图生视频/2073577575993139202.json, 视频生成/图生视频/2063147705244930049.json, 视频生成/图生视频/2064931292038385665.json, 视频生成/图生视频/调试Bernini Studio工作流-4步lora_rv2v_2102665904747270146.json, 视频生成/图生视频/2073745061728313345.json, 视频生成/图生视频/2073682935554854913.json, 视频生成/图生视频/2082366639907102721.json, 视频生成/图生视频/2082437380983844866.json, 视频生成/图生视频/2082454463452893186.json, 视频生成/图生视频/2082456967376883713.json, 视频生成/图生视频/2074035799124955138.json, 视频生成/图生视频/2064238678511280130.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_53

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/文生图/Bernini studio自由切换提示词前缀_2064529633915269122.json、视频生成/图生视频/2078439441877790721.json、视频生成/图生视频/2073592310989942786.json、视频生成/图生视频/2073584193665331202.json、视频生成/图生视频/2065400514141048833.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 20 个 workflow 都包含：
- `BerniniStudio`
- `CLIPLoader`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 18/20 个有
- `SetNode` —— 18/20 个有
- `VHS_LoadVideo` —— 17/20 个有
- `RTXVideoSuperResolution` —— 16/20 个有
- `ImageConcatMulti` —— 15/20 个有
- `Int` —— 12/20 个有
- `SimpleMath+` —— 10/20 个有
- `ComfyNumberConvert` —— 2/20 个有
- `VHS_VideoInfo` —— 2/20 个有
- `Fast Groups Bypasser (rgthree)` —— 1/20 个有
- `ShowAnything|Mie` —— 1/20 个有
- `Text` —— 1/20 个有
- `easy showAnything` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 20 | 75% |
| Prompt 约束强度(CFG) | 4 | 4 - 8 | 20 | 72% |
| 采样算法 | 1 | 1 - 1.5 | 20 | 89% |
| 调度器 | euler | - | 20 | 100% |
| 重绘幅度 | simple | - | 20 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，20 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 8，20 个样本
- 采样算法 中位数 1，观测区间 1 - 1.5，20 个样本，取值集中（一致性 89%）
- 调度器 最常用 euler，20 个样本，一致性 100%
- 重绘幅度 最常用 simple，20 个样本，一致性 100%
