---
name: unknown_workflow_sampler_clip_unet_84
type: Unknown Workflow
frequency: 12
level: weak
coverage: 0.933333
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, KSamplerAdvanced, LoadImage, ModelSamplingSD3, SaveVideo, UNETLoader, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2_首尾帧_1952176106529083393.json, 视频生成/图生视频/Wan2.2子弹时间LORA模型，只需要上传一张人物全身照，AI再现《黑客帝国》躲子弹_1983855179189620738.json, 视频生成/图生视频/Wan2.2最佳图生视频工作流（个人调试最佳版）_1950086411632467970.json, 视频生成/图生视频/Wan2.2首尾帧-ComfyUI官方版_1951916750197698561.json, 视频生成/图生视频/Wan3.0图生视频_2093297268513394689.json, 视频生成/图生视频/wan2.2-加速lora-4步极速-官方-图生视频_1956163238578847745.json, 视频生成/图生视频/wan2.2_一键万物打脸_1998363625523937282.json, 视频生成/图生视频/wan2.2图生视频_1997975012088905729.json, 视频生成/图生视频/wan2.2图生视频（kj模型加速版）_1950053385758269442.json, 视频生成/图生视频/wan2.2首尾帧_1962156046351536130.json, 视频生成/图生视频/wan2.2首尾帧视频生成VBVR符合视频逻辑，remixv3，_2041411003677679618.json, 视频生成/图生视频/第1期：Wan2.2图生视频——《Wan2.2从入门到精通》_1954125145533247489.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_84

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/Wan2.2_首尾帧_1952176106529083393.json、视频生成/图生视频/Wan2.2子弹时间LORA模型，只需要上传一张人物全身照，AI再现《黑客帝国》躲子弹_1983855179189620738.json、视频生成/图生视频/Wan2.2最佳图生视频工作流（个人调试最佳版）_1950086411632467970.json、视频生成/图生视频/Wan2.2首尾帧-ComfyUI官方版_1951916750197698561.json、视频生成/图生视频/Wan3.0图生视频_2093297268513394689.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `SaveVideo`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VAEDecode` —— 11/12 个有
- `WanImageToVideo` —— 7/12 个有
- `LoraLoaderModelOnly` —— 6/12 个有
- `WanFirstLastFrameToVideo` —— 5/12 个有
- `PathchSageAttentionKJ` —— 3/12 个有
- `Int` —— 2/12 个有
- `Label (rgthree)` —— 2/12 个有
- `SimpleMath+` —— 2/12 个有
- `ImpactFloat` —— 1/12 个有
- `MathExpression|pysssss` —— 1/12 个有
- `VAEDecodeTiled` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 12 | 58% |
| Prompt 约束强度(CFG) | 14 | 4 - 20 | 12 | 41% |
| 采样算法 | 2.25 | 1 - 4 | 12 | 41% |
| 调度器 | euler | - | 12 | 92% |
| 重绘幅度 | simple | - | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，12 个样本，一致性 58%
- Prompt 约束强度(CFG) 中位数 14，观测区间 4 - 20，12 个样本，取值分散，一致性仅 41%
- 采样算法 中位数 2.25，观测区间 1 - 4，12 个样本，取值分散，一致性仅 41%
- 调度器 最常用 euler，12 个样本，一致性 92%
- 重绘幅度 最常用 simple，12 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
