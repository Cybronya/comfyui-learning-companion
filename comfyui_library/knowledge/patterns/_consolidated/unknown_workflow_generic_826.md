---
name: unknown_workflow_generic_826
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.75
common_nodes: [LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, SaveImage, ShowText|pysssss]
problems: []
missing: []
members: [图片生成/反推提示词/三种方法图像反推提示词_1988322863948193794.json, 平台全量/图像反推，图片反推。提示词，prompt_1977918508329828354.json, 平台全量/色号识别(近似)_1962314401036615682.json, 平台全量/色号识别（近似值）_1961364595589976065.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_826

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/反推提示词/三种方法图像反推提示词_1988322863948193794.json、平台全量/图像反推，图片反推。提示词，prompt_1977918508329828354.json、平台全量/色号识别(近似)_1962314401036615682.json、平台全量/色号识别（近似值）_1961364595589976065.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 4 个 workflow 都包含：
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LoadImage`
- `SaveImage`
- `ShowText|pysssss`

**可变部分**（部分 workflow 才有）：
- `LayerMask: LoadFlorence2Model` —— 2/4 个有
- `LayerUtility: Florence2Image2Prompt` —— 2/4 个有
- `RH_Captioner` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
