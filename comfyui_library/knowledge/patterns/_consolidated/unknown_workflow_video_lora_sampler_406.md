---
name: unknown_workflow_video_lora_sampler_406
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9502
common_nodes: [BerniniBlockSwap, BerniniContextOptions, BerniniDirector, BerniniLoraSelectMulti, BerniniModelLoader, BerniniSamplerExtraArgs, BerniniScheduler, BerniniSetBlockSwap, BerniniSetLoRAs, BerniniT5Config, BerniniVAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2081023174543761410.json, 视频生成/图生视频/2065460725128192002.json, 视频生成/图生视频/2065713086010585089.json, 视频生成/图生视频/2066334769738244098.json, 视频生成/图生视频/2065453516738617346.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_406

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2081023174543761410.json、视频生成/图生视频/2065460725128192002.json、视频生成/图生视频/2065713086010585089.json、视频生成/图生视频/2066334769738244098.json、视频生成/图生视频/2065453516738617346.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `BerniniBlockSwap`
- `BerniniContextOptions`
- `BerniniDirector`
- `BerniniLoraSelectMulti`
- `BerniniModelLoader`
- `BerniniSamplerExtraArgs`
- `BerniniScheduler`
- `BerniniSetBlockSwap`
- `BerniniSetLoRAs`
- `BerniniT5Config`
- `BerniniVAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 4/5 个有
- `CreateVideo` —— 2/5 个有
- `ImageConcatMulti` —— 2/5 个有
- `SaveVideo` —— 2/5 个有
- `CR Text` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
