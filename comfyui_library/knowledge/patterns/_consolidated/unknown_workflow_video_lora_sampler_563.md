---
name: unknown_workflow_video_lora_sampler_563
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.7465
common_nodes: [BasicGuider, BasicScheduler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyLoader, MiniMaxH3EasyOutput, RandomNoise, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMaxH3参考图生视频_2094795058393468929.json, 视频生成/图生视频/MiniMaxH3参考图生视频_2097348758643240962.json, 视频生成/图生视频/MinimaxH3 Easy动作迁移人物替换1080高画质 角色替换 服装替换+全节点注释_2088895118051991553.json, 视频生成/图生视频/稳定性优化MinimaxH3 Easy动作迁移人物替换1080高画质 角色替换 服装替换+全节点注释_2093293369748451329.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_563

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3参考图生视频_2094795058393468929.json、视频生成/图生视频/MiniMaxH3参考图生视频_2097348758643240962.json、视频生成/图生视频/MinimaxH3 Easy动作迁移人物替换1080高画质 角色替换 服装替换+全节点注释_2088895118051991553.json、视频生成/图生视频/稳定性优化MinimaxH3 Easy动作迁移人物替换1080高画质 角色替换 服装替换+全节点注释_2093293369748451329.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyLoader`
- `MiniMaxH3EasyOutput`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `VAEDecodeAudio`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/4 个有
- `LoadVideo` —— 2/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/4 个有
- `ModelAttentionBackend` —— 2/4 个有
- `PrimitiveInt` —— 2/4 个有
- `RTXVideoSuperResolution` —— 2/4 个有
- `TextInput_` —— 2/4 个有
- `BiRefNetRMBG` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
