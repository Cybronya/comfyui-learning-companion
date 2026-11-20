---
name: unknown_workflow_video_lora_sampler_658
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.93875
common_nodes: [BerniniBlockSwap, BerniniContextEmbeds, BerniniContextOptions, BerniniDecode, BerniniLoraSelectMulti, BerniniModelLoader, BerniniSampler, BerniniSamplerExtraArgs, BerniniScheduler, BerniniSetBlockSwap, BerniniSetLoRAs, BerniniTextEncodeCached, BerniniVAELoader, ComfyNumberConvert, INTConstant, PrimitiveStringMultiline, RunningHub Deepcleaner, Seed (rgthree), SimpleMath+, VHS_VideoCombine, 孤海注释]
problems: []
missing: []
members: [平台全量/Bernini参考图主体替换视频主体_2069696206166650882.json, 平台全量/Bernini参考图物品替换视频物品_2069708177758838786.json, 平台全量/Bernini提示词修改视频_2069685282273845249.json, 视频生成/图生视频/Bernini多参生视频_2069422136309145602.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_658

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/Bernini参考图主体替换视频主体_2069696206166650882.json、平台全量/Bernini参考图物品替换视频物品_2069708177758838786.json、平台全量/Bernini提示词修改视频_2069685282273845249.json、视频生成/图生视频/Bernini多参生视频_2069422136309145602.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `BerniniBlockSwap`
- `BerniniContextEmbeds`
- `BerniniContextOptions`
- `BerniniDecode`
- `BerniniLoraSelectMulti`
- `BerniniModelLoader`
- `BerniniSampler`
- `BerniniSamplerExtraArgs`
- `BerniniScheduler`
- `BerniniSetBlockSwap`
- `BerniniSetLoRAs`
- `BerniniTextEncodeCached`
- `BerniniVAELoader`
- `ComfyNumberConvert`
- `INTConstant`
- `PrimitiveStringMultiline`
- `RunningHub Deepcleaner`
- `Seed (rgthree)`
- `SimpleMath+`
- `VHS_VideoCombine`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `VHS_LoadVideo` —— 3/4 个有
- `VHS_VideoInfoLoaded` —— 3/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
